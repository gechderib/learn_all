from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,authentication_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth import authenticate, login
from .models import CustomUser
from rest_framework.authtoken.models import Token
from commons.middlewares import isRoleExist, isAdminRoleExist
from commons.permission import IsAdmin, IsSuperUser
from rest_framework.parsers import MultiPartParser, FormParser

import cloudinary
from cloudinary.uploader import upload
import os

@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if(not isRoleExist(request)):
            return Response({"message":"Role doesn't exist please check your request"}, status=status.HTTP_400_BAD_REQUEST)        
        if isAdminRoleExist(request):
            return Response({"message":"You are not allowed to add an admin"}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        print(users)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsSuperUser])
def register_admin(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if(not isRoleExist(request)):
            return Response({"message":"Role doesn't exist please check your request"}, status=status.HTTP_400_BAD_REQUEST)        
        if not isAdminRoleExist(request):
            return Response({"message":"You are not allowed to register renter or owner"}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        phone_number = serializer.validated_data['phone_number']
        password = serializer.validated_data['password']
        
        try:
            user = CustomUser.objects.get(phone_number=phone_number, password=password)
        except CustomUser.DoesNotExist:
            return Response({'message':'customer not found'}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)

        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful', 'token':token.key, 'created':created}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_logout(request):
    request.auth.delete()
    return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
