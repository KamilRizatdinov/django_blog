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
        post1 = create_post('Post#1', 'Post#1 text', 0, timezone.now())
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_posts_list'], [f'<Post: {str(post1)}>'])

    def test_post_by_publication_date_ordering(self):
        """
        If there are several posts with the same views, they
        should be arranged in the publication_date descending order.
        """
        post1 = create_post('Post#1', 'Post#1 text', 0, timezone.now())
        post2 = create_post('Post#2', 'Post#2 text', 0, timezone.now() - datetime.timedelta(days=1))
        post3 = create_post('Post#3', 'Post#3 text', 0, timezone.now() - datetime.timedelta(days=10))
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_posts_list'], [
            f'<Post: {str(post1)}>',
            f'<Post: {str(post2)}>',
            f'<Post: {str(post3)}>',
        ])

    def test_post_by_views_ordering(self):
        """
        If there are several posts with the same publication_date,
        they should be arranged in the views descending order.
        """
        post1 = create_post('Post#1', 'Post#1 text', 10, timezone.now())
        post2 = create_post('Post#2', 'Post#2 text', 5, timezone.now())
        post3 = create_post('Post#3', 'Post#3 text', 1, timezone.now())
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_posts_list'], [
            f'<Post: {str(post1)}>',
            f'<Post: {str(post2)}>',
            f'<Post: {str(post3)}>',
        ])

    def test_post_by_publication_date_and_views_ordering(self):
        """
        If there are several posts, they should be arranged
        firts in the publication_date descending order,
        second in the views descending order.
        """
        post1 = create_post('Post#1', 'Post#1 text', 5, timezone.now())
        post2 = create_post('Post#2', 'Post#2 text', 1, timezone.now())
        post3 = create_post('Post#3', 'Post#3 text', 10, timezone.now() - datetime.timedelta(days=10))
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_posts_list'], [
            f'<Post: {str(post1)}>',
            f'<Post: {str(post2)}>',
            f'<Post: {str(post3)}>',
        ])
