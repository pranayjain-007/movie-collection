from django.db import models

# Movie model/Schema for Database.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    director = models.CharField(max_length=100)
