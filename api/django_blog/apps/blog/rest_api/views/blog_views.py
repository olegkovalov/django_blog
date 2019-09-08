from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django_blog.apps.blog.models import Post
from django_blog.apps.blog.rest_api.serializers.post import PostSerializer


class PostListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = PostSerializer
    queryset = Post.objects.active()


class PostDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = PostSerializer
    queryset = Post.objects.active()
