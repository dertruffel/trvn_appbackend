from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from urllib3 import HTTPResponse

from .serializers import CarCreateSerializer, PostCreateSerializer
from accounts.forms import CarForm

@renderer_classes((JSONRenderer, TemplateHTMLRenderer))
def AddCar(request):
    try:
        data = CarForm(request.POST)
        file = request.FILES['image']
        if data.is_valid():
            car = data.save()
            car.image = file
            car.save()
            return render(request, 'index.html')
        else:
            print(data.errors)
            return render(request, 'create-car.html', {'form': data})
    except Exception as e:
        print(e)
        return render(request, 'create-car.html', {'form': data})
class AddPost(APIView):
    def post(self, request):
        data = request.data
        serializer = PostCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'index.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)