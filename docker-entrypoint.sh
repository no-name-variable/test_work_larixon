#!/bin/sh

cd django_application

python manage.py collectstatic --noinput --clear
python manage.py migrate --noinput
uwsgi --ini config/server/uwsgi.ini --stats :3031 --stats-http

