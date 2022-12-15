from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from urllib3 import HTTPResponse

from .forms import CarForm, PostForm
from .models import Car


@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def AddCar(request):
    try:
        data = CarForm(request.POST)
        file = request.FILES['image']
        if data.is_valid():
            car = data.save()
            car.owner = request.user
            car.image = file
            car.save()
            return render(request, 'index.html')
        else:
            print(data.errors)
            return render(request, 'create-car.html', {'form': data})
    except Exception as e:
        print(e)
        return render(request, 'create-car.html', {'form': data})


@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def AddPost(request):
    try:
        data = PostForm(request.POST)
        if data.is_valid():
            data.save()
            return render(request, 'index.html')
        else:
            print(data.errors)
            return render(request, 'create-post.html', {'form': data})
    except Exception as e:
        print(e)
        return render(request, 'create-post.html', {'form': data})


@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def BuyCar(request, id):
    try:
        car = Car.objects.get(id=id)
        if car.price <= request.user.money and car.for_sale and car.owner != request.user:
            request.user.money -= car.price
            request.user.save()
            car.owner.money += car.price
            car.for_sale = False
            car.owner = request.user
            car.save()
            return render(request, 'index.html')
        else:
            return render(request, 'index.html', {'error': 'Not enough money'})
    except Exception as e:
        print(e)
        return render(request, 'index.html', {'error': 'Something went wrong'})