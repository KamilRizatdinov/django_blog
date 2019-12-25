from django.test import TestCase
from django.shortcuts import reverse


# Create your tests here.
class BlogIndexViewTests(TestCase):
    def test_status_code(self):
        """
        If the page is loaded, response contains appropriate status code.
        """
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)

    def test_no_posts(self):
        """
        If no posts exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No posts are available')
        self.assertQuerysetEqual(response.context['latest_posts_list'], [])
