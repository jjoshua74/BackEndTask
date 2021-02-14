# Units tests are also something new to me. For some reason the 'from .models import Article' doesn't work in this file.
# I can't figure out what is causing the import error - so this file does not run. I have added a few examples of
# how I would have attempted to run unit tests. I did not add unit tests for the whole project, since the file does
# not actually work and trying to fix the import error has delayed me to the point where I don't think I will submit on
# time if I still try to finish all unit tests.

# sorry

import unittest
from os import name
from .models import Article
from django.utils import timezone

class BackEndTaskTests(unittest.TestCase):

    def create_article(self, title="Test title", content="This is the test content", author="Joshua"):
        return Article.objects.create(title=title, content=content, date_created=timezone.now(), date_modified=timezone.now(), author=author)

    def test_article_creation(self):
        a = self.create_article()
        self.assertTrue(isinstance(a, Article))
        self.assertEqual(a.__unicode__(), a.title)

    def test_article_list_view(self):
        import requests
        import json
        x = requests.post("http://127.0.0.1:8000/articles", data=None)

        try:
            request = json.loads(x.text)

            if request['Result'] == 'ok':
                print("test article list - success")
        except Exception as e:
            raise Exception(e)


if name == 'main':
    unittest.main()
