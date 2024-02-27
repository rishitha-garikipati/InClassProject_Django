from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=120)
    director = models.TextField(max_length=100)
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
