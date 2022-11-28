from django.shortcuts import render

from accounts.forms import CarForm

from api.models import Car


def index(request):
    return render(request, 'index.html',{'cars': Car.objects.all()})

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
    return render(request, 'cars.html')

def car_details(request, id):
    return render(request, 'car-details.html', {'car': Car.objects.get(id=id)})

def create_car(request):
    return render(request, 'create-car.html', {'form': CarForm})

