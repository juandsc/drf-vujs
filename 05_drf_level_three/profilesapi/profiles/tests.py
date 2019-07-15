import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer
from profiles.models import Profile, ProfileStatus


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            'username': 'test-case-user',
            'email': 'test-case-user@profiles.com',
            'password1': 'user2019', 'password2': 'user2019'
        }
        response = self.client.post('/api/rest-auth/registration/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):

    # list_url = reverse('profile-list')

    def setUp(self):
        self.list_url = reverse('profile-list')
        self.user = User.objects.create_user(
            username='test-user', password='thepassword'
        )
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_profile_list_authentication(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authentication(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse('profile-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'test-user')

    def test_profile_update_by_owner(self):
        response = self.client.put(
            reverse('profile-detail', kwargs={'pk': 1}),
            {'city': 'cartagena', 'bio': 'ahora es costeno'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            {
                'id': 1, 'user': 'test-user', 'bio': 'ahora es costeno',
                'city': 'cartagena', 'avatar': None
            }
        )

    def test_profile_update_by_random_user(self):
        self.random_user = User.objects.create_user(
            username='random-user', password='thepassword'
        )
        self.client.force_authenticate(user=self.random_user)
        response = self.client.put(
            reverse('profile-detail', kwargs={'pk': 1}),
            {'bio': 'ahora es de la estrella'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ProfileStatusViewSetTestCase(APITestCase):

    url = reverse('status-list')
    def setUp(self):
        # self.url = reverse('status-list')
        self.user = User.objects.create_user(
            username='test-user', password='thepassword'
        )
        self.status = ProfileStatus.objects.create(
            user_profile=self.user.profile, status='status test'
        )
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_status_list_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_status_create(self):
        data = {'status': 'another status'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user_profile'], 'test-user')
        self.assertEqual(response.data['status'], 'another status')

    def test_single_status_retrieve(self):
        serializer_data = ProfileStatusSerializer(instance=self.status).data
        response = self.client.get(reverse('status-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_status_update_owner(self):
        data = {'status': 'an update'}
        response = self.client.put(
            reverse('status-detail', kwargs={'pk': 1}), data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'an update')

    def test_status_update_random_user(self):
        self.random_user = User.objects.create_user(
            username='random-user', password='thepassword'
        )
        self.client.force_authenticate(user=self.random_user)
        data = {'status': 'you have been hacked!!'}
        response = self.client.put(
            reverse('status-detail', kwargs={'pk': 1}), data=data
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)