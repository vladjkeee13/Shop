from django.test import TestCase, Client
from django.urls import reverse


class TestView(TestCase):

    fixtures = [
        'core/fixtures/users.json'
    ]

    def setUp(self):
        self.client = Client()

    def test_main_page(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_add_review(self):
        response = self.client.get(reverse('core:add-review'))
        self.assertEqual(response.status_code, 302)

    def test_add_review_logged_in(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('core:add-review'))
        self.assertEqual(response.status_code, 200)


