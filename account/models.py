from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('tech', 'Tech'),
        ('customer', 'Customer'),
    ]
    # adding the custom field here
    role = models.CharField(max_length=20, choices=ROLES, default='customer')
    profile_pic = models.CharField(max_length=100, null=True)
    pass