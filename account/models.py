from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):

    # adding the custom field here
    phone_number = models.CharField(max_length=15,unique=True,null=False,blank=False)
    username = models.CharField(max_length=15,unique=True, blank=True, null=True)
    roles = ArrayField(models.CharField(max_length=20), blank=True, default=list)
    profile_pic = models.CharField(max_length=100, null=True)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name','password']

    pass