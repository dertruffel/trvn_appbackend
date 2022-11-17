from rest_framework import serializers

from .models import Car, Post


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'name', 'model', 'year', 'price', 'created_at', 'updated_at')

class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'name', 'model', 'year', 'price', 'created_at', 'updated_at')

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'image', 'created_at', 'updated_at')

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'image', 'created_at', 'updated_at')

