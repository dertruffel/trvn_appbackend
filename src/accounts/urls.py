from rest_framework import routers
from django.urls import path, include

from accounts.views import UserRegister

router = routers.SimpleRouter()



urlpatterns = [
    path('userregister/', UserRegister.as_view(), name='user_register'),

]
