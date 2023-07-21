from django.urls import path
from .api import MovieListAPIView, MovieDetailAPIView


urlpatterns = [
    path('movies/', MovieListAPIView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
]
