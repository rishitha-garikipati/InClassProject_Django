from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField(blank=False,primary_key=True)
    sname = models.CharField(max_length=100,blank=False)

    class Meta:
        db_table='student_table'

from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField(blank=False,primary_key=True)
    sname=models.CharField(max_length=100, blank=False)

    class Meta:
        db_table='student_table'
class Employee(models.Model):
    emp_id=models.IntegerField(blank=False,primary_key=True)
    emp_name=models.CharField(blank=False,max_length=100)
    emp_desig=models.CharField(blank=False,max_length=100)

    class Meta:
        db_table='employee'