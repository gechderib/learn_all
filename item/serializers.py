from rest_framework import serializers
from .models import Item
class ItemSerializer:

    class Meta:
        model = Item
        fields = ('id', 'name','description','category','subcategory','postedBy','images')


