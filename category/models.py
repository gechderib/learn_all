from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, unique=False)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, unique=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='subcategories')

    def __str__(self):
        return f"{self.category.name} - {self.name}"
