from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username', 'first_name', 'last_name', 'is_admin', 'phone_number', 'created_at', 'updated_at')