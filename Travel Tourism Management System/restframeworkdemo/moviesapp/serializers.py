from rest_framework import serializers
from .models import Movie
class MovieSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fiels = '__all__'