from django.db import models
from item.models import Item
# Create your models here.

class SubCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, unique=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='subcategories')

    def __str__(self):
        return f"{self.category.name} - {self.name}"
class RentHistory(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE,)