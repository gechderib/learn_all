from rest_framework import serializers
from .models import Item
from category.serializers import SubCategorySerializer, CategorySerializer
from account.serializers import UserSerializer
class ItemSerializer(serializers.ModelSerializer):
    
    subcategory = SubCategorySerializer(many=False, read_only=True)
    postedBy = UserSerializer(many=False, read_only=True)
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'



