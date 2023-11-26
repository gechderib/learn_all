from rest_framework import serializers
from .models import Item
from category.serializers import SubCategorySerializer, CategorySerializer
from account.serializers import UserSerializer
class ItemSerializer:
    subcategories = SubCategorySerializer(many=False, read_only=True)
    category = CategorySerializer()
    postedBy = UserSerializer(many=False,)
    class Meta:
        model = Item
        fields = ('id', 'name','description','category','subcategory','postedBy','images')


