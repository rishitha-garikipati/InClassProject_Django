from django.urls import path
from .views import CreateMovieListView, AllMoviesListView

urlpatterns = [
    path('movies/',CreateMovieListView.as_view(),name="movie-list-create"),
    path('movies/all/',AllMoviesListView.as_view(),name="all-movies-list",)
]