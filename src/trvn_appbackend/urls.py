from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

api_urlpatterns = [
    path('accounts/', include('accounts.urls')),


    ]


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('docs/', include('docs.urls'), name='docs'),
    path('api/', include('api.urls'), name='api'),
    path('', include('frontpages.urls'), name='frontpages'),

]
admin.site.site_header = "TRVN Admin"
admin.site.site_title = "TRVN Admin Portal"
admin.site.index_title = "Welcome to TRVN Admin Panel"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

