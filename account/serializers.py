from rest_framework import serializers
from .models import CustomUser
import phonenumbers


# def validate_phone_number(value):
#     try:
#         parsed_number = phonenumbers.parse(value, None)
#         if not phonenumbers.is_valid_number(parsed_number):
#             raise serializers.ValidationError("Invalid phone number")
#     except NumberFormatException:
#         raise serializers.ValidationError("Invalid phone number format")


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    roles = serializers.ListSerializer(child=serializers.CharField(max_length=20), default=["renter"])
    profile_pic = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email','phone_number','first_name', 'last_name','profile_pic',"roles")
    
class UserLoginSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField()

