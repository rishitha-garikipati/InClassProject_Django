

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    img = models.ImageField(upload_to="")

    class Meta:
        db_table = "users"