from rest_framework import serializers

from django_blog.apps.account.models import User
from django_blog.apps.blog.models import Tag, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('pk', 'name',)


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)
    author = UserSerializer(required=False, read_only=True)
    serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Post
        fields = ('pk', 'title', 'text', 'tags', 'author', 'image',)
