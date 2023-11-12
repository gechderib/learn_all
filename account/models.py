from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    # adding the custom field here
    profile_pic = models.CharField(max_length=100, null=True)
    pass