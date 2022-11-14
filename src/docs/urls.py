from django.conf import settings
from django.urls import path

from drf_spectacular import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
# from drf_yasg import openapi, views
# from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = []

if settings.DEBUG:
    # schema_view = get_schema_view(
    #     openapi.Info(title='DevsCNTR API documentation', default_version='v1'),
    #     public=True,
    #     permission_classes=(permissions.AllowAny,)
    # )
    #
    # urlpatterns += [
    #     path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # ]

    urlpatterns += [
        path('', SpectacularAPIView.as_view(), name='schema'),
        path('schema/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
        ]

