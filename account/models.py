from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.
class CustomUser(AbstractUser):

    # adding the custom field here
    phone_number = models.CharField(max_length=15,unique=True,null=False,blank=False)
    username = models.CharField(max_length=15,unique=True, blank=True, null=True)
    roles = ArrayField(models.CharField(max_length=20), blank=True, default=list)
    profile_pic = models.ImageField(upload_to=upload_to, max_length=100000, null=True)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name','password','username']

    pass