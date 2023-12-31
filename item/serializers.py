from rest_framework import serializers
from .models import Item
from category.serializers import SubCategorySerializer, CategorySerializer
from account.serializers import UserSerializer,UserSerializerGet
from category.models import SubCategory, Category
from account.models import CustomUser

class ItemCreateSerializer(serializers.ModelSerializer):
    subcategory = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    postedBy = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    

    class Meta:
        model = Item
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    
    subcategory = SubCategorySerializer(many=False, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    postedBy = UserSerializerGet(many=False, read_only=True)
    status = serializers.SerializerMethodField()
    embedings = serializers.ListField(write_only=True)

    def get_status(self, obj):
        return obj.get_status_display()

    
    class Meta:
        model = Item
        fields = '__all__'




