from django.db import models

from apps.django_common.models import TimestampModel


class Category(TimestampModel):
    name: str = models.CharField(max_length=256, null=True, blank=True)

    adverts: models.QuerySet["Advert"]


class City(TimestampModel):
    name: str = models.CharField(max_length=256, null=True, blank=True)

    adverts: models.QuerySet["Advert"]


class Advert(TimestampModel):
    title: str = models.CharField(max_length=256, null=True, blank=True)
    description: str = models.TextField(max_length=1024, null=True, blank=True)
    views: int = models.IntegerField(default=0)

    city_id: int
    city: "City" = models.ForeignKey(
        'market.City', on_delete=models.SET_NULL, null=True, blank=True, related_name='adverts'
    )

    category_id: int
    category: "Category" = models.ForeignKey(
        'market.Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='adverts'
    )
