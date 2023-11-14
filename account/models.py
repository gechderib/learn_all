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
    phone_number = models.CharField(max_length=15,unique=True,null=False,blank=False)
    username = models.CharField(max_length=15,unique=True, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLES, default='customer')
    profile_pic = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name','password']

    pass