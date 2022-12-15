from django.urls import path, include

from frontpages import views
from accounts import views as accounts_views
from api import views as api_views

urlpatterns = [
    path('', views.index, name='index'),
    path('addcar/', api_views.AddCar, name='addcar'),
    path('addpost/', api_views.AddPost, name='add-post'),
    path('postdetails/<int:id>', views.post_details, name='post-details'),
    path('posts/', views.posts, name='posts'),
    path('register/', accounts_views.UserRegisterRender, name='user_register_render'),
    path('registerapi/', accounts_views.UserRegister, name='user_register'),
    path('loginapi/', accounts_views.UserLogin, name='user_login'),
    path('logoutapi/', accounts_views.UserLogout, name='user_logout'),
    path('login/', accounts_views.UserLoginRender, name='user_login_render'),
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
    path('car-details/<int:id>/', views.car_details, name='car_details'),
    path('create-car/', views.create_car, name='create-car'),
    path('buy-car/<int:id>/', api_views.BuyCar, name='buy-car'),

]




