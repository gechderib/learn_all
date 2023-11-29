from django.db import models
from django.contrib.postgres.fields import ArrayField
from category.models import Category, SubCategory
from account.models import CustomUser
# Create your models here
# .
class Item(models.Model):

    STATUS_CHOICES = [
        ('100', 'Available'),
        ('101', 'Rented'),
        ('102', 'Sold'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default=100, max_length=100)
    
    rent_price = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(null=True,blank=True, max_digits=10, decimal_places=2, default=0)
    available_for_sell = models.BooleanField(null=False,blank=False, default=False)

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="subcategory")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    postedBy = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False, related_name='postedBy')
    
    images = ArrayField(models.ImageField(upload_to='item_images/'), blank=True, null=True)


