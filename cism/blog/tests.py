from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from django.urls import reverse
from blog.models import Post, Like

User = get_user_model()


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_user_1 = User.objects.create_user(username='user99', email='3bngnbdjn@mail.com', password='Qq123456')
        cls.test_user_1.save()
        cls.test_user_2 = User.objects.create_user(username='user100', email='4bngnbdjn@mail.com', password='Qq123456')
        cls.test_user_2.save()
        cls.test_post = Post.objects.create(author='test_author', topic='test_topic', body='test_body')
        cls.unauthorized_api_client = APIClient()
        cls.test_user_1_api_client = APIClient()
        cls.test_user_1_api_client.force_authenticate(cls.test_user_1)
        cls.test_user_2_api_client = APIClient()
        cls.test_user_2_api_client.force_authenticate(cls.test_user_2)


class PostTest(BaseTest):
    def test_create_post(self):
        self.assertEquals(self.test_post.author, 'test_author')
        self.assertEquals(self.test_post.topic, 'test_topic')
        self.assertEquals(self.test_post.body, 'test_body')
        self.assertEquals(self.test_post.likes.count(), 0)


class LikeTest(BaseTest):
    def test_like_if_user_unauthorized(self):
        resp = self.client.post(reverse('blog:like', args=[self.test_post.id]))
        self.assertEquals(resp.status_code, status.HTTP_302_FOUND)
        likes_count = self.test_post.likes.count()
        self.assertEquals(likes_count, 0)

    def test_like_if_user_authorized(self):
        login = self.client.login(username='user99', password='Qq123456')
        resp = self.client.post(reverse('blog:like', args=[self.test_post.id]))
        self.assertEquals(resp.status_code, status.HTTP_302_FOUND)
        likes_count = self.test_post.likes.count()
        self.assertEquals(likes_count, 1)
        resp_2 = self.client.post(reverse('blog:like', args=[self.test_post.id]))
        likes_count = self.test_post.likes.count()
        self.assertEquals(likes_count, 0)

    def test_like_unique_together(self):
        like_1 = Like.objects.create(liker=self.test_user_1, liked_post=self.test_post)
        try:
            like_2 = Like.objects.create(liker=self.test_user_1, liked_post=self.test_post)
            is_error = False
        except IntegrityError as er:
            is_error = True
        self.assertTrue(is_error)


class APIPostTest(BaseTest):

    def test_get_token(self):
        resp = self.client.post('/api/v1/auth/token/login/', data={'password': 'Qq123456', 'username': 'user99'})
        self.assertEquals(resp.status_code, status.HTTP_200_OK)

    def test_get_posts(self):
        resp = self.client.get('/api/v1/posts/')
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        resp_post = self.client.get(f'/api/v1/posts/{self.test_post.id}/')
        self.assertEquals(resp_post.status_code, status.HTTP_200_OK)

    def test_post_posts(self):
        resp = self.client.post('/api/v1/posts/', data={"author": "test_author", "topic": "test_topic",
                                                        "body": "test_body"})
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)

    # def test_put_post_(self):
    #     resp = self.client.put(f'/api/v1/posts/{self.test_post.id}/',
    #                            {"author": "test_put_author", "topic": "test_put_topic", "body": "test_put_body"})
    #     print(resp)

    def test_delete_post(self):
        resp = self.client.delete(f'/api/v1/posts/{self.test_post.id}/')
        self.assertEquals(resp.status_code, status.HTTP_204_NO_CONTENT)

    def test_like_post_user_unauthorized(self):
        resp = self.client.post(f'/api/v1/posts/{self.test_post.id}/like/')
        self.assertEquals(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_like_post_user_authorized(self):
        resp = self.test_user_1_api_client.post(f'/api/v1/posts/{self.test_post.id}/like/')
        self.assertEquals(resp.status_code, status.HTTP_201_CREATED)
        resp = self.test_user_1_api_client.post(f'/api/v1/posts/{self.test_post.id}/like/')
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
