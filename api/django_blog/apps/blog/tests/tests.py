from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.views import status

from django_blog.apps.blog.models import Post, Tag


class PostListCreateAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('api-post-list', kwargs={'version': 'v1'})

    def test_create_post(self):
        self.assertEquals(
            Post.objects.count(),
            0
        )
        data = {
            'title': 'title',
            'text': 'text'
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            Post.objects.count(),
            1
        )
        post = Post.objects.first()
        self.assertEquals(
            post.title,
            data['title']
        )
        self.assertEquals(
            post.text,
            data['text']
        )

    def test_get_post_list(self):
        tag = Tag(name='tag_name')
        tag.save()
        post = Post(title='title1', text='text1')
        post.save()
        post.tags.add(tag)

        response = self.client.get(self.url)
        response_json = response.json()
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            len(response_json),
            1
        )
        data = response_json[0]
        self.assertEquals(
            data['title'],
            post.title
        )
        self.assertEquals(
            data['text'],
            post.text
        )
        self.assertEquals(
            data['tags'][0]['name'],
            tag.name
        )


class PostDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        self.post = Post(title='title2', text='text2')
        self.post.save()
        self.url = reverse('api-post-details', kwargs={'version': 'v1', 'pk': self.post.pk})

    def test_get_post_details(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        self.assertEquals(
            data['pk'],
            str(self.post.pk)
        )
        self.assertEquals(
            data['title'],
            self.post.title
        )
        self.assertEquals(
            data['text'],
            self.post.text
        )

    def test_update_post(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        data['title'] = 'new_title'
        data['text'] = 'new_text'
        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.post.refresh_from_db()
        self.assertEquals(
            self.post.title,
            data['title']
        )
        self.assertEquals(
            self.post.text,
            data['text']
        )

    def test_delete_post(self):
        self.assertEquals(
            Post.objects.count(),
            1
        )
        response = self.client.delete(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEquals(
            Post.objects.count(),
            0
        )
