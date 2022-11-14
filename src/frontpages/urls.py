from django.urls import path, include

from src.frontpages import views
from src.accounts import views as accounts_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', accounts_views.UserRegisterRender, name='user_register_render'),
]