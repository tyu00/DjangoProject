from django.test import TestCase
from django.test import Client
from core import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = models.User.objects.create(
            name='Первый',
            email='pervi@gmail.com',
            phone='88888888888',
            is_rare=True
        )

    def test_index(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/redirect/')
        self.assertEqual(response.status_code, 302)

    def test_user_data_presence(self):
        user_count = models.User.objects.filter(name='Первый', email='pervi@gmail.com', phone='88888888888', ).count()
        self.assertEqual(user_count, 1)

    def test_post_list_view(self):
        response = self.client.get('/post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/post_list.html')
