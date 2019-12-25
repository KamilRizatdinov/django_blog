from django.test import TestCase
from django.shortcuts import reverse
from django.utils import timezone
from blog.models import Post
import datetime


def create_post(header, text, views, publication_date):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    return Post.objects.create(
        header=header,
        text=text,
        views=views,
        publication_date=publication_date,
    )


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

    def test_one_post(self):
        """
        If there exist exactly one post, it need to be in 'latest_posts_list' in context.
        """
        post = create_post('Post#1', 'Post#1 text', 10, timezone.now())
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_posts_list'], [f'<Post: {str(post)}>'])
