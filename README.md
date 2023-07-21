# movie-collection

The movie collection project consists of few REST API endpoints for a movie rental application built using the Django Python framework.

## Requirements

- Python (version 3.11.3)

Python Libraries:

- django (version 4.2.2)
- djangorestframework==3.14.0

Make sure both the libraries are installed. Install them inside the project folder using pip commmand. (eg. pip install djangorestframework==3.14.0)

## Installation

1. Extract the zip file. Place the movie_collection folder at a suitable location.

2. Change into the project directory:

	cd movie_collection

3. Install the project dependencies:

	pip install django
	pip install djangorestframework

4. Set up the database:

	python manage.py migrate

5. Create a superuser for administrative access.(optional - There is already a dummy_user created inside the project):

	python manage.py createsuperuser

Enter some dummy credentials to create superuser.

## Usage

To run the development server, use the following command:

	python.exe .\manage.py runserver

The server will start running at http://localhost:8000/. You can access the API endpoints using a tool like Postman.

NOTE - For Authentication, you can use following dummy credentials which must be already present or the superuser credentials:
username: dummy_user
password: dummy_password

The credentials will be required only once to access the APIs in browser. A session will be created which will be used further for authentication.

## API Endpoints

You can use the following methods & urls in Postman or Web Browser. Make sure to set Authorization Type=Basic auth with username & password if using Postman.

- 'GET /api/movies/': Retrieve a list of all movies.
- 'GET /api/movies/{id}/': Retrieve a specific movie by its ID.
- 'POST /api/movies/': Create a new movie.
- 'PUT /api/movies/{id}/': Update an existing movie.
- 'PATCH /api/movies/{id}/': Partially update an existing movie.
- 'DELETE /api/movies/{id}/': Delete a movie.

NOTE - Please refer to the code comments in movie_collection\api_app\api.py file for complete details on request/response formats.

## Pagination

You can make a get request for specific number of movies on a single page.
Pass an integer value to the following query parameters viz. movies_per_page, page.

For Example - localhost:8000/api/movies/?movies_per_page=10&page=2

## Filtering

Filtering is supported for genre & director fields.
Pass a string to the following query parameters viz. genre, director.

For Example - localhost:8000/api/movies/?genre=[{'id': 35, 'name': 'Comedy'}, {'id': 27, 'name': 'Horror'}]

## Testing

To run the unit tests, use the following command:

	python.exe .\manage.py test

There are 8 test case present. If all the test case passes, "OK" will be returned in the shell.
