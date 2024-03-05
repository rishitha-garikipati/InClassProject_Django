from django.urls import path
from .views import CreateMovieListView, AllMoviesListView, MovieDeleteView, MovieUpdateView

urlpatterns = [
    path('movies/',CreateMovieListView.as_view(),name="movie-list-create"),
    path('movies/all/',AllMoviesListView.as_view(),name="all-moives-list"),
    path('movies/delete/<int:pk>',MovieDeleteView.as_view(),name="delete-movie"),
    path('movies/update/<int:pk>',MovieUpdateView.as_view(),name="update-movie"),
]
