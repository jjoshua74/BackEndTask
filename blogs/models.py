from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(default="anonymous", max_length=100)

    class Meta:
        ordering = ['title']


class Comment(models.Model):
    content = models.TextField()
    user_name = models.CharField(max_length=100)
    article_id = models.IntegerField()

    class Meta:
        ordering = ['article_id']