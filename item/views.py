from django.shortcuts import render
from .models import Item
from .serializers import ItemSerializer, ItemCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes,parser_classes
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from cloudinary import uploader

# Create your views here.
@api_view(['GET'])
def get_all_items(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_one_item(request,pk):
    if request.method == 'GET':
        try:
            items = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response("Item doesnot exist with the provided id")
        serializer = ItemSerializer(items, many=False)
        return Response(serializer.data)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def add_item(request):
    if request.method == 'POST':
        serializer = ItemCreateSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            category = serializer.validated_data.get("category")
            subcategory = serializer.validated_data.get('subcategory')
            postedBy = serializer.validated_data.get('postedBy')
            description = serializer.validated_data.get('description')
            status = serializer.validated_data.get('status')
            rent_price = serializer.validated_data.get('rent_price')
            available_for_sell = serializer.validated_data.get('available_for_sell')
            selling_price = serializer.validated_data.get('selling_price')
            images = request.FILES.getlist('images')
            # image_urls = [uploader.upload(image)['secure_url'] for image in images]
            image_urls = []
            print(len(images))
            for i in range(len(images)):
                print("Processing image:", i + 1)
                print("Image path:", images[i])

                result = uploader.upload(images[i])
                print("Upload result:", result)

                image_urls.append(result['secure_url'])
            # instance = Item.objects.create(name=name, category=category,subcategory=subcategory,postedBy=postedBy,description=description,status=status,rent_price=rent_price,available_for_sell=available_for_sell, selling_price=selling_price,image_urls=','.join(image_urls))
            print(image_urls)
            # serializer = ItemCreateSerializer(instance)

            # serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

