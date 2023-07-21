from .models import Movie
from .serializers import MovieSerializer
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# /api/movies/ endpoint. (movie_list)
class MovieListAPIView(APIView):

    # Authenticating User.
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        movies = Movie.objects.all()

        # Apply filtering if mentioned in url. (For eg. localhost:8000/api/movies/?director=Pranay)
        genre = request.query_params.get('genre')
        director = request.query_params.get('director')
        if genre:
            movies = movies.filter(genre__icontains=genre)
        if director:
            movies = movies.filter(director__icontains=director)
        
        # Apply pagination if mentioned in url. (For eg. localhost:8000/api/movies/?movies_per_page=10&page=2)
        movies_per_page = request.query_params.get('movies_per_page')
        if movies_per_page:
            page = request.query_params.get('page', 1)
            paginator = Paginator(movies, movies_per_page)
            try:
                movies = paginator.page(page)
            except PageNotAnInteger:
                movies = paginator.page(1)
            except EmptyPage:
                movies = paginator.page(paginator.num_pages)

        serializer = MovieSerializer(movies, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        # Create a new movie
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# api/movies/{id} endpoint (movie_detail)
class MovieDetailAPIView(APIView):

    def get(self, request, pk):
        # Retrieve a specific movie by its ID
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        # Create/Update all the fields of a movie.
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        # Partially update an existing movie.
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)