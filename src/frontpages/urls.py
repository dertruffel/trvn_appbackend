from django.urls import path, include

from frontpages import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', accounts_views.UserRegisterRender, name='user_register_render'),
    # path('login/', accounts_views.UserLoginRender, name='user_login_render'),
    # path('logout/', accounts_views.UserLogoutRender, name='user_logout_render'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('team/', views.team, name='team'),
    path('cars/', views.cars, name='cars'),
    path('car-details/', views.car_details, name='car_details'),

]




