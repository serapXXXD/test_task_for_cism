from rest_framework import status
from blog.tests import BaseTest


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
