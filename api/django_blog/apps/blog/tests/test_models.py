from django.test import TestCase

from django_blog.apps.blog.models import Post, Tag


class PostTestCase(TestCase):
    def test_post(self):
        self.assertEquals(
            Post.objects.count(),
            0
        )
        Post.objects.create(
            title='active', text='text', is_active=True
        )
        Post.objects.create(
            title='inactive', text='text', is_active=False
        )
        self.assertEquals(
            Post.objects.count(),
            2
        )
        active_posts = Post.objects.active()
        self.assertEquals(
            active_posts.count(),
            1
        )
        inactive_posts = Post.objects.inactive()
        self.assertEquals(
            inactive_posts.count(),
            1
        )


class TagTestCase(TestCase):
    def test_tag(self):
        self.assertEquals(
            Tag.objects.count(),
            0
        )
        Tag.objects.create(name='name')
        self.assertEquals(
            Tag.objects.count(),
            1
        )
