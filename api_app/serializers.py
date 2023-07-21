from rest_framework import serializers
from .models import Movie

# Serializing data to return JSON Response.
class MovieSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255, required=True)
    genre = serializers.CharField(max_length=100, required=True)
    release_date = serializers.DateField(format='%Y-%m-%d', required=True)
    director = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'release_date', 'director']

