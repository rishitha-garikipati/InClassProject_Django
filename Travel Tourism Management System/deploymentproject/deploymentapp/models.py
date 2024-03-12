from django.db import models

# Create your models here.

class Student(models.Model):
    sname = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    fees = models.CharField(max_length=100)


class Meta:
    db_table = 'student'