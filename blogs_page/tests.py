from urllib import response
from django.test import TestCase
from django.urls import reverse

from .models import Blogs

# Create your tests here.

class BlogsTests(TestCase):

    def setUp(self):
        self.blog = Blogs.objects.create(
            title = "First blog",
            author = "Shivam Kumar",
            content = "this is the content of the first blog",
        )

    def test_blog_listning(self):
        self.assertEqual(f'{self.blog.title}', 'First blog')
        self.assertEqual(f'{self.blog.author}', 'Shivam Kumar')
        self.assertEqual(f'{self.blog.content}', 'this is the content of the first blog')

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First blog')
        self.assertTemplateUsed(response, 'blogs/blog_list.html')

    def test_blog_detail_view(self):
        response = self.client.get(self.blog.get_absolute_url())
        no_response = self.client.get('/blogs/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'First blog')
        self.assertTemplateUsed(response, 'blogs/blogs_detail.html')