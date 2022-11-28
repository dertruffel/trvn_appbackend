from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from accounts.serializers import UserSerializer

from accounts.forms import SignUpForm, SignInForm


def UserRegisterRender(request):
    return render(request, 'user_register.html', {'form': SignUpForm})


@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def UserRegister(request):
    data = SignUpForm(request.POST)
    if data.is_valid():
        data.save()
        return render(request, 'index.html', {'form': data})
    else:
        return render(request, 'user_register.html', {'form': data})


def UserLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    login(request, user)
    if user is not None:
        return render(request, 'index.html', {'user': user, 'access': True})
    else:
        return render(request, 'user_login.html')

def UserLoginRender(request):
    return render(request, 'user_login.html', {'form': SignInForm})

def UserLogout(request):
    logout(request)
    return render(request, 'index.html', {'access': False})