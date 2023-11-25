from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth import authenticate, login
from .models import CustomUser
from rest_framework.authtoken.models import Token
from commons.middlewares import isRoleExist, isAdminRoleExist, isOtherRoleExist
from commons.permission import IsAdmin, IsSuperUser

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        isRoleExist(request)
        if(not isRoleExist(request)):
            return Response("Role doesn't exist please check your request", status=status.HTTP_400_BAD_REQUEST)        
        if isAdminRoleExist(request):
            return Response("You are not allowed to register admin", status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsSuperUser])
def register_admin(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        isRoleExist(request)
        if(not isRoleExist(request)):
            return Response("Role doesn't exist please check your request", status=status.HTTP_400_BAD_REQUEST)        
        if not isAdminRoleExist(request):
            return Response("You are not allowed to register renter or owner", status=status.HTTP_403_FORBIDDEN)
        if isOtherRoleExist(request):
            return Response("You can't add other role, only admin role is allowed", status=status.HTTP_403_FORBIDDEN)
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
