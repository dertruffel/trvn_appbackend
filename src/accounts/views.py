from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserSerializer


def UserRegisterRender(request):
    return render(request, 'user_register.html')

class UserRegister(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'index.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'index.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def UserLoginRender(request):
    return render(request, 'user_login.html')