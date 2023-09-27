from rest_framework import serializers

from apps.market import models


class AdvertSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name")
    city_name = serializers.CharField(source="city.name")

    class Meta:
        model = models.Advert
        fields = "title", "description", "views", "category_name", "city_name",