from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    roles = serializers.ListField(write_only=True)
    profile_pic = serializers.ImageField(required=False)
    
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email','phone_number','first_name', 'last_name','profile_pic',"roles")
    
class UserLoginSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField()

