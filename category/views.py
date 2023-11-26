from django.shortcuts import render
from .serializers import CategorySerializer, SubCategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from .models import Category, SubCategory
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from commons.permission import IsAdmin
from rest_framework.authentication import TokenAuthentication


# Create your views here.

@api_view(["GET"])
def get_all_main_category(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(["GET"])
def get_main_category_detail(request, pk):
    """
    Retrieve, categories.
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return JsonResponse({"message":"data with id not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)




@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsAdmin])
def addMainCategory(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["PUT","DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsAdmin])
def change_category_detail(request, pk):
    """
    Retrieve, update or delete a categories.
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return JsonResponse({"message":"data with id not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return HttpResponse(status=204)







# sub category views 




@api_view(["GET"])
def get_all_sub_category(request):
    if request.method == 'GET':
        sub_categories = SubCategory.objects.all()
        serializer = SubCategorySerializer(sub_categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(["GET"])
def get_sub_category_detail(request, pk):
    """
    Retrieve, categories.
    """
    try:
        sub_category = SubCategory.objects.get(pk=pk)
    except SubCategory.DoesNotExist:
        return JsonResponse({"message":"data with id not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubCategorySerializer(sub_category)
        return JsonResponse(serializer.data)





@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsAdmin])
def addSubCategory(request):
    if request.method == 'POST':
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["PUT","DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsAdmin])
def change_sub_category_detail(request, pk):
    """
    Retrieve, update or delete a categories.
    """
    try:
        sub_category = SubCategory.objects.get(pk=pk)
    except SubCategory.DoesNotExist:
        return JsonResponse({"message":"data with id not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SubCategorySerializer(sub_category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sub_category.delete()
        return HttpResponse(status=204)

