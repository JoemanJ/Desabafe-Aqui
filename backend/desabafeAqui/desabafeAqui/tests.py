from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status

class JWTTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testUser',
            'email': 'test@user.com',
            'password': 'testPassword123',
        }
        self.user = User.objects.create_user(username=self.user_data['username'],
                                             email=self.user_data['email'],
                                             password=self.user_data['password'],)
    def test_user_can_get_JWT_from_API(self):
        """
        Checks that a registered user can get a JWT by sending the right
        credentials to the token api.
        """
        url = reverse('token-obtain-pair')
        data = {
            'username': self.user_data['username'],
            'password': self.user_data['password'],
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_cant_get_JWT_from_API_with_wrong_credentials(self):
        """
        Checks that a user cannot get a JWT by sending wrong credentials to the
        token api.
        """
        url = reverse('token-obtain-pair')
        data = {
            'username': 'wrongUser',
            'password': 'wrongPassword',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access', response.data)
        self.assertNotIn('refresh', response.data)
