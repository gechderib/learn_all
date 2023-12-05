from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):

    # adding the custom field here
    phone_number = models.CharField(max_length=15,unique=True,null=False,blank=False)
    username = models.CharField(max_length=15,unique=True, blank=True, null=True)
    role = models.CharField(max_length=20, blank=False, default="renter")
    profile_pic = models.ImageField(upload_to='rent_all_user_profile',max_length=100000, null=True, blank=True)
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name','password','username','role']

    pass