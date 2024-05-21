from django.test import TestCase


class Tests(TestCase):
    def test_index(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/redirect/')
        self.assertEqual(response.status_code, 302)
