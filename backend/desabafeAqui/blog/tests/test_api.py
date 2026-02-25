from django.urls import reverse

from . import createTestUser
from ..models import Post, Comment

from rest_framework import status
from rest_framework.test import APITestCase


class PostAPITest(APITestCase):
    def setUp(self):
        self.user = createTestUser()
        self.post = Post.objects.create(author=self.user,
                                        text="Test post")
        self.list_url = reverse('post-list')
        self.detail_url = reverse('post-detail', kwargs={'slug': self.post.slug})

    def test_get_posts_list_returns_OK(self):
        """
        Checks that a GET on the posts list returns 200 OK
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_posts_list_returns_registered_post(self):
        """
        Checks that a GET on the posts list returns the test post
        """
        response = self.client.get(self.list_url)
        self.assertContains(response, "Test post")

    def test_get_posts_detail_returns_registered_post(self):
        """
        Checks that a GET on a specific post returns the test post
        """
        response = self.client.get(self.detail_url)
        self.assertContains(response, "Test post")

    def test_create_post_api(self):
        """
        Checks that a POST on the posts api can create a new post
        """
        self.client.force_login(user=self.user)

        new_post_data = {"text": "New post"}
        response = self.client.post(self.list_url, new_post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.last().author, self.user)

    #TODO: write tests for the other actions

class CommentAPITest(APITestCase):
    def setUp(self):
        self.user = createTestUser()
        self.post = Post.objects.create(author=self.user,
                                        text="Test post")
        self.comment = Comment.objects.create(author=self.user,
                                              post=self.post,
                                              text="Test comment")
        self.list_url = reverse('comment-list')
        self.detail_url = reverse('comment-detail', kwargs={'pk': self.comment.id})

    def test_get_comments_list_returns_OK(self):
        """
        Checks that a GET on the comments list returns 200 OK
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_comments_list_returns_registered_comment(self):
        """
        Checks that a GET on the comments list returns the test comment
        """
        response = self.client.get(self.list_url)
        self.assertContains(response, "Test comment")

    def test_get_comments_detail_returns_registered_comment(self):
        """
        Checks that a GET on a specific comment returns the test comment
        """
        response = self.client.get(self.detail_url)
        self.assertContains(response, "Test comment")

    def test_create_comment_api(self):
        """
        Checks that a POST on the comments api can create a new comment
        """
        self.client.force_login(user=self.user)

        new_comment_data = {"post": self.post.slug,
                            "text": "New comment"}
        response = self.client.post(self.list_url, new_comment_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    #TODO: write tests for the other actions