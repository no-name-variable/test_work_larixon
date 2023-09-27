from django.contrib import admin
from django.urls import path, include


from apps.api.urls import urlpatterns as api_urlpatterns


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns))
]

