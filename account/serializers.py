from rest_framework import serializers
from .models import CustomUser
import phonenumbers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # roles = serializers.ListSerializer(child=serializers.CharField(max_length=20), default=["renter"])
    profile_pic = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email','phone_number','first_name', 'last_name','profile_pic')
    
class UserLoginSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField()

