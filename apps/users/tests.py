from django.test import TestCase

# Create your tests here.

# API Test cases
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from Archive.apps.goods.models import Users
from requests.auth import HTTPBasicAuth
from rest_framework.test import APIRequestFactory
from django.test.client import encode_multipart, RequestFactory


class UsersTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('users-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users.objects.count(), 1)
        self.assertEqual(Users.objects.get().name, 'DabApps')

# Test Headers & Authentication

client = CoreAPIClient()
client.session.auth = HTTPBasicAuth('user', 'pass')
client.session.headers.update({'x-test': 'true'})


# APIRequestFactory


# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'})


# Create a JSON POST request
factory = APIRequestFactory()
request = factory.post('/notes/', json.dumps({'title': 'new idea'}), content_type='application/json')


factory = APIRequestFactory()
request = factory.put('/notes/547/', {'title': 'remember to email dave'})



factory = RequestFactory()
data = {'title': 'remember to email dave'}
content = encode_multipart('BoUnDaRyStRiNg', data)
content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
request = factory.put('/notes/547/', content, content_type=content_type)
