from rest_framework import routers
from django.urls import path, include

from .views import *

# router = routers.SimpleRouter()
# router.register('addcar', AddCar, basename='addcar')
# router.register('addpost', AddPost, basename='addpost')

# create namespace api
app_name = 'api'

urlpatterns = [
     # path('', include(router.urls)),
     # path('addcar/', AddCar.as_view(), name='add-car'),
     # path('addpost/', AddPost.as_view(), name='add-post'),


]
