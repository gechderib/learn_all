from rest_framework import serializers
from .models import CustomUser
import json


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)
    profile_pic = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email','phone_number','first_name', 'last_name','profile_pic','role']
    
class UserLoginSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField()

