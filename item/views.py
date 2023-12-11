from django.shortcuts import render
from .models import Item
from .serializers import ItemSerializer, ItemCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes,parser_classes
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from cloudinary import uploader
from commons.middlewares import isImageExist,isAddingImage
from commons.utils import  delete_cloudinary_image
from commons.permission import IsOwner
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
import openai
from openai import OpenAI
import spacy
from spacy.matcher import PhraseMatcher

client = openai.OpenAI(api_key='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')

# @api_view(['GET'])
# def get_all_items(request):
#     search_term = request.query_params.get('search', '')
#     if search_term:
#         # Perform a case-insensitive search on name, category, and subcategory
#         queryset = Item.objects.filter(
#             Q(name__icontains=search_term) |
#             Q(category__name__icontains=search_term) |
#             Q(subcategory__name__icontains=search_term)
#         )
#     else:
#         queryset = Item.objects.all()

#     serializer = ItemSerializer(queryset, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_all_items(request):
    search_term = request.query_params.get('search', '')
    if search_term:
        # Set up OpenAI API key
        openai.api_key = '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'

        # # Use OpenAI's Completions API to generate relevant text
        # response = openai.Completion.create(
        #     engine="text-davinci-003",  # You can experiment with different engines
        #     prompt=f"Find products related to: {search_term}",
        #     max_tokens=50  # Adjust based on the desired length of generated text
        # )

        response = client.embeddings.create(
            input="Your text string goes here",
            model="text-embedding-ada-002"
        )

        # # Extract relevant information from the OpenAI API response
        # generated_text = response['choices'][0]['text']
        # print(generated_text)
        # generated_keywords = generated_text.split()
        print(response.data[0].embedding)

        # Use the generated keywords to filter products
        queryset = Item.objects.filter(
            name__icontains=response.data[0]
        )

    else:
        queryset = Item.objects.all()

    serializer = ItemSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@permission_classes([IsOwner])
@parser_classes([MultiPartParser, FormParser])
def add_item(request):
    if request.method == 'POST':
        serializer = ItemCreateSerializer(data=request.data)
        if serializer.is_valid():
            if(not isImageExist(request)):
                return Response({"message":"you should select atleast two image"}, status=401)
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

            image_urls = []
            item_folder = "item_images"
            for image in images:
                result = uploader.upload(image, folder=item_folder)
                image_urls.append(result['secure_url'])
            instance = Item.objects.create(name=name, category=category,subcategory=subcategory,postedBy=postedBy,description=description,status=status,rent_price=rent_price,available_for_sell=available_for_sell, selling_price=selling_price,image_urls=image_urls)
            serializer = ItemCreateSerializer(instance)

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_item(request, pk):
    instance = get_object_or_404(Item, pk=pk)
    if not (request.user and request.user == instance.postedBy):
        return Response({"message":"You can only update you own item"})
    if request.method in ['PUT','PATCH']:
        serializer = ItemCreateSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            # Check if images are being updated
            if 'images' in request.FILES:
                item_folder = "item_images"
                if isAddingImage(request):
                    # add the new image to cloudinary                
                    new_image_urls = []
                    for new_image in request.FILES.getlist('images'):
                        result = uploader.upload(new_image, folder=item_folder)
                        new_image_urls.append(result['secure_url'])

                    instance.image_urls.extend(new_image_urls)
                else:
                    # remove the previous image from cloudinary
                    for img_url in instance.image_urls:
                        parts = img_url.split('/')
                        public_id = item_folder +"/"+ parts[-1].split('.')[0]
                        delete_cloudinary_image(public_id)
                    # add the new image to cloudinary                
                    new_image_urls = []
                    for new_image in request.FILES.getlist('images'):
                        result = uploader.upload(new_image, folder=item_folder)
                        new_image_urls.append(result['secure_url'])

                    instance.image_urls = new_image_urls
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    return Response({"message": "Invalid HTTP method"}, status=405)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_item(request, pk):
    instance = get_object_or_404(Item,pk=pk)
    if not (request.user and request.user == instance.postedBy):
        return Response({"message":"You can only delete you own item"})

    if request.method == "DELETE":
        item_folder = "item_images"
        for img_url in instance.image_urls:
            parts = img_url.split('/')
            public_id = item_folder +"/"+ parts[-1].split('.')[0]
            delete_cloudinary_image(public_id)

        instance.delete()
        return HttpResponse(status=204)