FROM python:3.10-slim-buster as base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWIRTEBYTECODE=1 \
    PYSETUP_PATH=/opt/pysetup \
    APPLICATION_PATH=/usr/app
ENV VENV_PATH=$PYSETUP_PATH/.venv
ENV PATH=$VENV_PATH/bin:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends libpq5

FROM base as builder

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME=/opt/poetry/ \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.3.1
ENV PATH=$POETRY_HOME/bin:$PATH

WORKDIR $PYSETUP_PATH

RUN apt-get -y update \
    && apt-get install -y build-essential gettext libpq-dev curl \
    && curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml ./
COPY django_application/ ./django_application/

RUN poetry install -n --no-root --no-dev


FROM builder as dev-builder
RUN poetry install -n --no-root


FROM base as app-base

ENV PORT=8000 \
    STATIC_ROOT=/static \
    MEDIA_ROOT=/media/public \
    PRIVATE_MEDIA_ROOT=/media/private
EXPOSE 8000 8002 8003 8004 8005 8006 8007 8008

WORKDIR $APPLICATION_PATH

COPY django_application/ ./django_application/
COPY docker-entrypoint.sh ./
RUN chmod +x docker-entrypoint.sh


FROM app-base as development

ENV POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    VIRTUAL_ENV=$VENV_PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

ENV DJANGO_SETTINGS_MODULE=config.settings.development
ENV DEVELOPMENT=true

COPY --from=dev-builder $POETRY_HOME $POETRY_HOME
COPY --from=dev-builder $VENV_PATH $VENV_PATH


CMD ["./docker-entrypoint.sh"]
