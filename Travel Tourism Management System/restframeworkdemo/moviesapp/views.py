from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
# Create your views here.

class CreateMovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.create()
    serializer_class = MovieSerializer

class AllMoviesListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
