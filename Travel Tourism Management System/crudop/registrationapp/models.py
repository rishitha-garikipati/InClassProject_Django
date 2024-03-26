from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Users(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)

