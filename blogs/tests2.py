import unittest
from os import name
from .models import Article
from django.utils import timezone

class ModelTests(unittest.TestCase):

    def create_article(self, title="Test title", content="This is the test content", author="Joshua"):
        return Article.objects.create(title=title, content=content, date_created=timezone.now(), date_modified=timezone.now(), author=author)

    def test_article_creation(self):
        a = self.create_article()
        self.assertTrue(isinstance(a, Article))
        self.assertEqual(a.__unicode__(), a.title)

if name == 'main':
    unittest.main()