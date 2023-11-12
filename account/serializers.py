from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name','profile_pic')
    
    # def create(self,validated_data):
    #     user = CustomUser.objects.create_user(**validated_data)
    #     return user

