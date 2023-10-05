
import unittest

from django.test import TestCase
from django.test import Client
from django.urls import reverse


class ViewAboutTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_base_one(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 301)



class IndexTest(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)



class ErrorTest(TestCase):
    def test_error(self):
        response = self.client.get('error_page')
        self.assertEqual(response.status_code, 404)





