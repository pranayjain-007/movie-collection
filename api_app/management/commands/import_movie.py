"""

Note - The following script is only needed for importing database. No need to execute the script if database is already present.

The following script is used to import the required fields from the csv file to the SQLite Database.
It must be called after creating initial migrations.
Run the following command from Django root folder = python manage.py import_movie "Path_of_csv_file"

"""

import csv
from django.core.management.base import BaseCommand
from api_app.models import Movie
from datetime import datetime

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, **options):
        file_path = options['file_path']
        self.import_movies_from_csv(file_path)

    def import_movies_from_csv(self, file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')
            
            for row in reader:
                # Access the columns using the column names
                title = row['title']
                genre = row['genres']
                release_date_str = row['release_date']
                director = row['director']

                if release_date_str:
                    try:
                        release_date = datetime.strptime(release_date_str, '%d-%m-%Y').date()
                    except ValueError:
                        release_date = None
                        continue

                movie = Movie(title=title, genre=genre, release_date=release_date, director=director)
                movie.save()

