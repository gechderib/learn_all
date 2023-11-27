from rest_framework import serializers
from .models import Category, SubCategory
# from item.serializers import ItemSerializer
# from account.serializers import UserSerializer
class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)
    # items = ItemSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
