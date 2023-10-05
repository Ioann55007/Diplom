from django.test import TestCase
import unittest
from django.test import Client
from django.urls import reverse


class ViewPostTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        response = self.client.get('/news-1')
        self.assertEqual(response.status_code, 200)



class DetailPostTest(TestCase):
    def test_post_detail(self, slug=None):
        response = self.client.get(reverse('part_post:news-post'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['post'], slug)








