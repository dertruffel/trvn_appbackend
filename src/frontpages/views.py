from calendar import monthrange
from datetime import date, datetime

from django.shortcuts import render

from api.forms import CarForm

from api.models import Car,Post

from api.forms import PostForm

from accounts.models import User, Event
from django.template import RequestContext


def index(request):
    return render(request, 'index.html',{'cars': Car.objects.filter(for_sale=True).order_by('-views')[:3], 'posts': Post.objects.all().order_by('-created_at')[:3]})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def team(request):
    return render(request, 'team.html')

def cars(request):
    return render(request, 'cars.html', {'cars': Car.objects.filter(for_sale=True).order_by('-created_at')})

def car_details(request, id):
    car = Car.objects.get(id=id)
    car.views += 1
    car.save()
    return render(request, 'car-details.html', {'car': Car.objects.get(id=id)})

def create_car(request):
    return render(request, 'create-car.html', {'form': CarForm})

def create_post(request):
    return render(request, 'create-post.html', {'form': PostForm})

def posts(request):
    return render(request, 'posts.html', {'posts': Post.objects.all().order_by('-created_at')})

def post_details(request, id):
    return render(request, 'post-details.html', {'post': Post.objects.get(id=id)})

def my_cars(request):
    user = User.objects.filter(id=request.user.id).first()
    return render(request, 'my_cars.html', {'cars': Car.objects.filter(owner=user).order_by('-created_at')})

