from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .models import Comment
from django.http import Http404
from .serializers import ArticleSerializer
from .serializers import CommentSerializer


class ArticleList(generics.ListCreateAPIView):
    """
    List all articles, or create a new article.
    """
    # only allows admins to send POST requests (add articles)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(APIView):
    """
    Retrieve or delete an article instance.
    """
    # only allows admins to delete articles
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def delete_comments(self, pk):
        """
        used to delete all the comments for a corresponding article.
        """
        try:
            comments = Comment.objects.all()
            # filter to only contain comments for specified article (article_id)
            comments = list(filter(lambda x: x.article_id == pk, comments))

            #loop through and delete all comments
            for comment in comments:
                comment.delete()

        except Comment.DoesNotExist:
            pass

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        self.delete_comments(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):
    """
    List all comments of a specified article, or create a new commment.
    """

    def get_object(self, article_id):
        """
        Will find the comments that belong to an article.
        :param article_id: the id of the article to which the comments belong
        :returns: a list of the comments belonging to an article
        """
        try:
            comments = Comment.objects.all()
            #filter to only contain comments for specified article (article_id)
            comments = list(filter(lambda x: x.article_id == article_id , comments))
            return comments
        except Comment.DoesNotExist:
            raise Http404

    def article_exists(self, article_id):
        """
        checks if an article exists
        :param article_id: the id of the article to be checked
        :returns boolean: True if the article exists
        :raises Http404: if the article does not exist
        """
        try:
            Article.objects.get(pk=article_id)
            return True
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, article_id, format=None):
        comments = self.get_object(article_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, article_id, format=None):

        # check if the article exists before a comment can be added
        if self.article_exists(article_id):
            request.data["article_id"] = article_id
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a comment instance.
    """
    # only allows admins to delete articles
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
