from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from urllib3 import HTTPResponse

from .serializers import CarCreateSerializer, PostCreateSerializer

class AddCar(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            print(data)
            serializer = CarCreateSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return render(request, 'index.html')
            return render(request, 'create-car.html', {'error': 'Error'})
        except HTTPResponse as e:
            return render(request, 'create-car.html', {'error': e})

class AddPost(APIView):
    def post(self, request):
        data = request.data
        serializer = PostCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'index.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)