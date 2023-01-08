from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from urllib3 import HTTPResponse

from .forms import CarForm, PostForm, ChangeCarPriceForm, ContactForm, CommentForm
from .models import Car, Post, Comment
from django.contrib.auth import get_user_model
User = get_user_model()


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


@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def ChangeOnSaleCar(request, id):
    try:
        user = User.objects.filter(id=request.user.id).first()
        car = Car.objects.get(id=id)
        if car.owner == user:
            if car.for_sale:
                car.for_sale = False
            else:
                car.for_sale = True
            car.save()
            return render(request, 'my_cars.html', {'cars': Car.objects.filter(owner=user).order_by('-created_at')})
        else:
            return render(request, 'my_cars.html', {'error': 'Not your car'},{'cars': Car.objects.filter(owner=user).order_by('-created_at')})
    except Exception as e:
        print(e)
        return render(request, 'index.html', {'error': 'Something went wrong'})

@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def ChangeCarPrice(request, carid):
    try:
        user = User.objects.filter(id=request.user.id).first()
        print(carid)
        car = Car.objects.get(id=carid)
        print(carid)
        if car.owner == user:
            data = ChangeCarPriceForm(request.POST)
            if data.is_valid():
                car.price = data.cleaned_data['price']
                car.save()
                return render(request, 'my_cars.html', {'cars': Car.objects.filter(owner=user).order_by('-created_at')})
            else:
                print(data.errors)
                return render(request, 'my_cars.html', {'form': data},{'cars': Car.objects.filter(owner=user).order_by('-created_at')})
        else:
            return render(request, 'my_cars.html', {'error': 'Not your car'},{'cars': Car.objects.filter(owner=user).order_by('-created_at')})
    except Exception as e:
        print(e)
        return render(request, 'index.html', {'error': 'Something went wrong'})

@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def Contact(request):
    if not User.objects.filter(id=request.user.id).first().is_authenticated:
        return render(request, 'index.html', {'error': 'You are not logged in'})
    try:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form.author = request.user
            return render(request, 'index.html')
        else:
            print(form.errors)
            return render(request, 'contact.html', {'form': form})
    except Exception as e:
        print(e)
        return render(request, 'contact.html', {'form': form})

@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def AddComment(request, postid):
    if not User.objects.filter(id=request.user.id).first().is_authenticated:
        return render(request, 'index.html', {'error': 'You need to login'})
    try:
        post = Post.objects.filter(id=postid).first()
        try:
            user = request.user
            print(post, postid)
            data = CommentForm(request.POST)
            comment_text = data['comment'].value()
            comment = Comment.objects.create(comment=comment_text)
            user.comments.add(comment)
            user.save()
            post.comments.add(comment)
            post.save()

            return render(request, 'post-details.html', {'posts': [post], 'forms': CommentForm})
        except Exception as e:
            print(e)
            return render(request, 'post-details.html', {'posts': [post], 'forms': CommentForm})
    except Exception as e:
        print(e)
        return render(request, 'index.html', {'error': 'Something went wrong'})