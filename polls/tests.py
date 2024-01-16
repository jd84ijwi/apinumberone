from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from polls import apiviews 

class TestPoll(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.uri = '/polls/polls/'
        self.view = apiviews.PollList.as_view()


    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'testuser',
            email='',
            password='api12345api'
        )
    
    def test_list(self):
        request = self.factory.get(self.uri,
            HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code)
                         )
        
    def test_list2(self):
        self.client.login(username='testuser', password='api12345api')
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code, received {0} instead.'
                         .format(response.status_code))
        

def test_create(self):
        self.client.login(username='testuser', password='api12345api')
        params = {
            'question': 'How are you doing?',
            'created_by': 1
             }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Respone Code, receiverd {0} instead.'
                         .format(response.status_code)
                         
                         )