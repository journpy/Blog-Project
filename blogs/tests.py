from django.test import TestCase
from .models import Blog

# Create your tests here.
class BlogTest(TestCase):

    def setUp(cls):
        Blog.objects.create(
            id=1,
            title='Test Title', 
            author='Uche', 
            content='This is just a test.'
            )

    def test_views_index(self):
        blog = Blog.objects.get(id=1)
        print(blog.date_created)
        self.assertEqual(blog.title, 'Test Title')
        self.assertEqual(blog.author, 'Uche')
