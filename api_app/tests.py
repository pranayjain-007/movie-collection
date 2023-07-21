from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Movie

# Test Module containing all the Test Cases.
class MovieAPITests(APITestCase):

    # Setting up Test User and Test Data.
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.movie = Movie.objects.create(title='Movie 1', genre='Action', release_date='2022-01-01', director='Director 1')

    # Testing GET method for /api/movie/ endpoint.
    def test_get_movie_list(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('movie_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Testing POST method for /api/movie/ endpoint.
    def test_post_movie_list(self):
        self.client.force_authenticate(user=self.user)
        movie_data = {
            'title': 'New Movie',
            'genre': 'Comedy',
            'release_date': '2022-05-01',
            'director': 'Jane Smith'
        }
        url = reverse('movie_list')
        response = self.client.post(url, movie_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], movie_data['title'])
        self.assertEqual(response.data['genre'], movie_data['genre'])
        self.assertEqual(response.data['release_date'], movie_data['release_date'])
        self.assertEqual(response.data['director'], movie_data['director'])

    # Testing PUT method for /api/movie/ endpoint. (Negative Scenario)
    def test_put_movie_detail(self):
        self.client.force_authenticate(user=self.user)
        updated_movie_data = {
            'title': 'Updated Movie',
            'genre': 'Drama',
            'release_date': '2022-10-15',
            'director': 'John Smith'
        }
        url = reverse('movie_list')
        response = self.client.put(url, updated_movie_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # Testing PATCH method for /api/movie/ endpoint. (Negative Scenario)
    def test_patch_movie_detail(self):
        self.client.force_authenticate(user=self.user)
        updated_movie_data = {
            'director': 'John Snow'
        }
        url = reverse('movie_list')
        response = self.client.patch(url, updated_movie_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # Testing DELETE method for /api/movie/ endpoint. (Negative Scenario)
    def test_delete_movie_list(self):
        self.client.force_authenticate(user=self.user)    
        url = reverse('movie_list')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # Testing GET method for /api/movie/{id} endpoint.
    def test_get_movie_detail(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('movie_detail', args=[self.movie.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.movie.title)
        self.assertEqual(response.data['genre'], self.movie.genre)
        self.assertEqual(response.data['release_date'], self.movie.release_date)
        self.assertEqual(response.data['director'], self.movie.director)

    # Testing POST method for /api/movie/{id} endpoint. (Negative Scenario)
    def test_post_movie_detail(self):
        self.client.force_authenticate(user=self.user)
        movie_data = {
            'title': 'New Movie',
            'genre': 'Comedy',
            'release_date': '2022-05-01',
            'director': 'Jane Smith'
        }
        url = reverse('movie_detail', args=[self.movie.pk])
        response = self.client.post(url, movie_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # Testing PUT method for /api/movie/{id} endpoint.
    def test_put_movie_detail(self):
        self.client.force_authenticate(user=self.user)
        updated_movie_data = {
            'title': 'Updated Movie',
            'genre': 'Drama',
            'release_date': '2022-10-15',
            'director': 'John Smith'
        }
        url = reverse('movie_detail', args=[self.movie.pk])
        response = self.client.put(url, updated_movie_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_movie_data['title'])
        self.assertEqual(response.data['genre'], updated_movie_data['genre'])
        self.assertEqual(response.data['release_date'], updated_movie_data['release_date'])
        self.assertEqual(response.data['director'], updated_movie_data['director'])

    # Testing PATCH method for /api/movie/{id} endpoint.
    def test_patch_movie_detail(self):
        self.client.force_authenticate(user=self.user)
        updated_movie_data = {
            'director': 'John Snow'
        }
        url = reverse('movie_detail', args=[self.movie.pk])
        response = self.client.patch(url, updated_movie_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.movie.title)
        self.assertEqual(response.data['genre'], self.movie.genre)
        self.assertEqual(response.data['release_date'], self.movie.release_date)
        self.assertEqual(response.data['director'], updated_movie_data['director'])

    # Testing DELETE method for /api/movie/{id} endpoint.
    def test_delete_movie_detail(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('movie_detail', args=[self.movie.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(response.data)