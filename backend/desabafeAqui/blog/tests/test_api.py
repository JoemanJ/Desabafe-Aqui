from django.urls import reverse
from django.contrib.auth.models import User

from . import createTestUser
from ..models import Post, Comment, UserProfile

from rest_framework import status
from rest_framework.test import APITestCase


class PostAPITest(APITestCase):
    def setUp(self):
        self.user = createTestUser()
        self.post = Post.objects.create(author=self.user,
                                        text="Test post")
        self.list_url = reverse('post-list')
        self.detail_url = reverse('post-detail', kwargs={'slug': self.post.slug})
        self.like_url = reverse('post-like', kwargs={'slug': self.post.slug})

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
        self.client.force_authenticate(user=self.user)

        new_post_data = {"text": "New post"}
        response = self.client.post(self.list_url, new_post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.last().author, self.user)

    def test_user_cant_delete_another_users_post(self):
        """
        Checks that a user can't delete another user's post
        """
        hacker = User.objects.create(username='hackerman', password='123212321')
        self.client.force_authenticate(user=hacker)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Post is still there
        self.assertEqual(Post.objects.count(), 1)

    def test_user_can_delete_their_own_post(self):
        """
        Checks that a user can delete their own post
        """
        self.client.force_authenticate(self.user)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymous_users_cant_like_posts(self):
        """
        Checks that a user that is not logged in (anonymous) can't like a post
        """
        response = self.client.post(self.like_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_can_like_a_post(self):
        """
        Checks that a user can like a post through the API
        """
        self.client.force_authenticate(self.user)

        response = self.client.post(self.like_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], "liked")
        self.post.refresh_from_db()
        self.assertEqual(self.post.likes.count(), 1)

    def test_user_can_unlike_a_previously_liked_post(self):
        """
        Checks that a user can unlike a post they have previously liked with a 
        POST request to the like endpoint
        """
        self.client.force_authenticate(self.user)

        self.client.post(self.like_url)
        response = self.client.post(self.like_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], "unliked")
        self.post.refresh_from_db()
        self.assertEqual(self.post.likes.count(), 0)

    def test_can_get_liked_count_from_post(self):
        """
        Checks that we can get the amount of likes a post has with a GET to the
        Posts endpoint
        """
        response = self.client.get(self.detail_url)

        self.assertContains(response, '"likes_count":0')

    def test_can_get_check_if_current_user_has_liked_post(self):
        """
        Checks that we can know if the current user has liked the post with a 
        GET call to the API
        """
        self.client.force_authenticate(self.user)

        response = self.client.post(self.like_url)
        response = self.client.get(self.detail_url)

        self.assertContains(response, '"is_liked":true')

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
        self.client.force_authenticate(user=self.user)

        new_comment_data = {"post": self.post.slug,
                            "text": "New comment"}
        response = self.client.post(self.list_url, new_comment_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_user_cant_delete_another_users_comment(self):
        """
        Checks that a user can't delete another user's comment
        """
        hacker = User.objects.create(username='hackerman', password='123212321')
        self.client.force_authenticate(user=hacker)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # comment is still there
        self.assertEqual(Comment.objects.count(), 1)

    def test_user_can_delete_their_own_comment(self):
        """
        Checks that a user can delete their own comment
        """
        self.client.force_authenticate(self.user)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ProfileAPITest(APITestCase):
    def setUp(self):
        self.user = createTestUser()
        self.profile = self.user.profile
        self.profile.bio = "Test profile bio"
        self.profile.save()
        self.list_url = reverse('profile-list')
        self.detail_url = reverse('profile-detail', 
                                  kwargs={'user__username': self.user.username})

    def test_get_profiles_list_returns_OK(self):
        """
        Checks that a GET on the profiles list returns 200 OK
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_profiles_list_returns_registered_profile(self):
        """
        Checks that a GET on the profiles list returns the test profile
        """
        response = self.client.get(self.list_url)
        self.assertContains(response, "Test profile")

    def test_get_profiles_detail_returns_registered_profile(self):
        """
        Checks that a GET on a specific profile returns the test profile
        """
        response = self.client.get(self.detail_url)
        self.assertContains(response, "Test profile")

    def test_user_cannot_delete_a_profile(self):
        """
        Checks that a user cannot delete their own profile
        TODO: Refactor this into more tests so check that no one can delete any
        profile
        """
        self.client.force_authenticate(self.user)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        # profile is still there
        self.assertEqual(UserProfile.objects.count(), 1)

class MiniProfileAPITest(APITestCase):
    def setUp(self):
        self.user = createTestUser()
        self.profile = self.user.profile
        self.profile.bio = "Test profile bio"
        self.profile.save()
        self.list_url = reverse('miniprofile-list')
        self.detail_url = reverse('miniprofile-detail', 
                                  kwargs={'user__username': self.user.username})

    def test_get_mini_profiles_list_returns_OK(self):
        """
        Checks that a GET on the miniprofiles list returns 200 OK
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_mini_profiles_list_returns_registered_profile(self):
        """
        Checks that a GET on the mini_profiles list returns the test profile
        """
        response = self.client.get(self.list_url)
        self.assertContains(response, self.user.username)

    def test_get_mini_profile_detail_returns_registered_profile(self):
        """
        Checks that a GET on a specific mini profile returns the test profile
        """
        response = self.client.get(self.detail_url)
        self.assertContains(response, self.user.username)