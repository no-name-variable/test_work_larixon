from django.urls import path, include

from apps.api.market.views import AdvertsListView, AdvertView

advert_urlpatterns = [
    path("advert-list/", AdvertsListView.as_view(), name="advert-list"),
    path("<int:advert_id>/advert/", AdvertView.as_view(), name='advert')
]

urlpatterns = [
    path('market/', include(advert_urlpatterns)),
    ]