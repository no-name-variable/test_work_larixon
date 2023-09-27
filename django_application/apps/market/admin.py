from django.contrib import admin

from apps.market import models as market_models


@admin.register(market_models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(market_models.City)
class CityAdmin(admin.ModelAdmin):
    ...


@admin.register(market_models.Advert)
class AdvertAdmin(admin.ModelAdmin):
    ...