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
        self.post = models.Post.objects.create(
            title='новый электромобиль',
            is_rare=True
        )

    def test_index(self):
        response = self.client.get('/index/')
        self.assertEquals(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/redirect/')
        self.assertEquals(response.status_code, 302)

    def test_user_data_presence(self):
        user_count = models.User.objects.filter(name='Первый', email='pervi@gmail.com', phone='88888888888',).count()
        self.assertEqual(user_count, 1)

    def test_post_data_presence(self):
        post_count = models.Post.objects.filter(title='новый электромобиль').count()
        self.assertEqual(post_count, 1)
