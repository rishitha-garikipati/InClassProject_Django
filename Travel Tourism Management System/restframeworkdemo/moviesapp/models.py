from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_lenght=120)
    director = models.TextField(max_lenght=100)
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
