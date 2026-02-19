from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Post, config

def createTestUser(username="TestUser", email="test@user.com",
                    password="testPassword"):
    """ 
    Creates a sample new user
    """
    newUser = User.objects.create(username=username,
                                    email=email,
                                    password=password)
    return newUser

# Create your tests here.
class UserProfileModelTest(TestCase):
    def setUp(self):
        self.newUser = createTestUser()
        pass
        
    
    def test_profile_is_created_when_user_is_created(self):
        """
        Checks that a new profile is created automatically when a new user is
        created 
        """
        self.assertIsNotNone(self.newUser.profile)

    def test_profile_is_empty_when_user_is_created(self):
        """
        Checks that the profile created automatically when a new user is created
        is empty, with no bio or profile picture
        """
        expected_bio = ""
        expected_profile_picture = ""

        self.assertEqual(self.newUser.profile.bio, expected_bio)
        self.assertEqual(self.newUser.profile.picture, expected_profile_picture)

    def test_profile_string_is_as_expected(self):
        """
        Checks if the profile's __str__ method returns the expected string
        """

        profile = self.newUser.profile
        expected_string = f"{self.newUser.username}'s (id: {self.newUser.pk}) profile"

        self.assertEqual(str(profile), expected_string)


class PostModelClass(TestCase):
    def setUp(self):
        self.newUser1 = createTestUser()
        self.newUser2 = createTestUser(username="TestUser2")

    def test_posts_are_assigned_to_the_right_user(self):
        """
        Checks that you can get the right user from different posts
        """
        post1= Post.objects.create(author=self.newUser1,
                                   text="newUser1's post")
        
        post2= Post.objects.create(author=self.newUser2,
                                   text="newUser2's post")
        
        self.assertEqual(post1.author, self.newUser1)
        self.assertEqual(post2.author, self.newUser2)

    def test_new_posts_receive_a_random_slug(self):
        """
        Checks that a new post automatically receives a random slug
        """
        post = Post.objects.create(author=self.newUser1,
                                   text="I should have a slug")
        
        self.assertIsNotNone(post.slug)

    def test_new_post_slugs_have_the_correct_size(self):
        """
        Checks that the slug generated for a post has the correct currently used
        size, defined by Post.__slug_size
        """
        post = Post.objects.create(author=self.newUser1,
                                   text=f"I should have a slug of size {config["POST_SLUG_SIZE"]}")
        
        self.assertEqual(len(post.slug), config["POST_SLUG_SIZE"])

    def test_post_string_is_as_expected(self):
        """
        Checks if the post's __str__ method returns the expected string
        """
        text1="Short post"
        text2="Looooooooooooooong poooooooooooooost"

        post1 = Post.objects.create(author=self.newUser1,
                                   text=text1)
        
        post2 = Post.objects.create(author=self.newUser2,
                                    text=text2)
        
        self.assertIn(self.newUser1.username, str(post1))
        self.assertIn(text1[:20], str(post1))
        self.assertIn(self.newUser2.username, str(post2))
        self.assertIn(text2[:20], str(post2))