from django.db import models
from django.contrib.postgres.fields import ArrayField
from category.models import Category, SubCategory
from account.models import CustomUser
# Create your models here
# .

class ItemManager(models.Manager):
    def create_item(self, name,description,status,rent_price,selling_price,available_for_sell,subcategory,category,postedBy,image_urls,embedings):
        item = self.create(name=name,description=description,status=status,rent_price=rent_price,selling_price=selling_price,available_for_sell=available_for_sell,subcategory=subcategory,category=category,postedBy=postedBy,image_urls=image_urls,embedings=embedings)
        # You can add additional logic here if needed
        return item
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
    
    image_urls = ArrayField(models.TextField(blank=False, null=False),default=list)  # Store image URLs as a comma-separated string
    embedings = ArrayField(models.TextField(blank=False, null=False), default=list)

    objects = ItemManager()  # Assign the custom manager

