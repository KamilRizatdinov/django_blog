from django.test import TestCase
from django.shortcuts import reverse


# Create your tests here.
class BlogIndexViewTests(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
