from rest_framework import serializers
from .models import Item
from category.serializers import SubCategorySerializer, CategorySerializer
from account.serializers import UserSerializer
from category.models import SubCategory, Category
from account.models import CustomUser

class ItemSerializer(serializers.ModelSerializer):

    # subcategory = SubCategorySerializer(many=False)
    # category = CategorySerializer(many=False)
    # postedBy = UserSerializer(many=False,)

    subcategory = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    postedBy = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    
    class Meta:
        model = Item
        fields = '__all__'



