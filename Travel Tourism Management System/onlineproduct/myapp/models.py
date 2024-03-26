from django.db import models

# Create your models here.
class Product(models.Model):
    pid = models.IntegerField(blank=False,primary_key=True)
    pname = models.CharField(max_length=100,blank=False)
    price = models.CharField(max_length=100,blank=False)