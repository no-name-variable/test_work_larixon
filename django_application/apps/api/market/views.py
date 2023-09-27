from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.api.market import serializers
from apps.market.models import Advert


class AdvertsListView(GenericAPIView):
    serializer_class = serializers.AdvertSerializer

    def get(self, request: Request) -> Response:
        del request
        adverts = Advert.objects.select_related(
            'city',
            'category',
        ).all()

        if adverts:
            serializer = self.get_serializer(adverts, many=True)
            return Response(serializer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)


class AdvertView(GenericAPIView):
    serializer_class = serializers.AdvertSerializer

    def get(self, request: Request, advert_id: int) -> Response:
        del request
        advert = Advert.objects.select_related(
            'city',
            'category',
        ).filter(id=advert_id).first()

        if advert:
            advert.views += 1
            advert.save(update_fields=['views', 'updated_at'])
            serializer = self.get_serializer(advert)
            return Response(serializer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)