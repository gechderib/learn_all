from django.db import models
from django.contrib.postgres.fields import ArrayField
from category.models import Category, SubCategory
from account.models import CustomUser
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='subcategory')
    postedBy = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False, related_name='postedBy')
    images = ArrayField(models.ImageField(upload_to='item_images/'), blank=True, null=True)
