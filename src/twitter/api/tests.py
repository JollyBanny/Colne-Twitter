# Create your tests here.

from django.test import TestCase

class UsersTestCase(TestCase):
    def test_simple(self):
        self.assertEqual(1+1,2)

    def test_list_users(self):
        response = self.client.get('/v1/users/')
        self.assertEqual(response.status_code, 200)

    def test_new_follow_correct(self):
        self.client.force_login(self.user1)
        response = self.client.post('/v1/follow/Kevin')
        self.assertEqual(response.status_code, 201)