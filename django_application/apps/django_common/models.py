import datetime

from django.db import models
from django.utils.timezone import localtime


class TimestampModel(models.Model):
    created_at: datetime.datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at: datetime.datetime = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        abstract = True

    @property
    def created_at_pretty(self) -> str:
        return localtime(self.created_at).strftime("%d.%m.%Y %H:%M:%S")
    created_at_pretty.fget.short_description = "Время создания"

    @property
    def updated_at_pretty(self) -> str:
        return localtime(self.updated_at).strftime("%d.%m.%Y %H:%M:%S")

    created_at_pretty.fget.short_description = "Время обновления"