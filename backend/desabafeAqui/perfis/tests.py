from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

# Create your tests here.
class UserProfileModelTest(TestCase):
    def setUp(self):
        pass
        
    def createTestUser(self, username="TestUser", email="test@user.com",
                       password="testPassword"):
        """ 
        Creates a sample new user
        """
        newUser = User.objects.create(username=username,
                                      email=email,
                                      password=password)
        return newUser
    
    def test_profile_is_created_when_user_is_created(self):
        """
        Checks that a new profile is created automatically when a new user is
        created 
        """
        newUser = self.createTestUser()

        self.assertIsNotNone(newUser.profile)

    def test_profile_is_empty_when_user_is_created(self):
        """
        Checks that the profile created automatically when a new user is created
        is empty, with no bio or profile picture
        """
        newUser = self.createTestUser()

        expected_bio = ""
        expected_profile_picture = ""

        self.assertEqual(newUser.profile.bio, expected_bio)
        self.assertEqual(newUser.profile.picture, expected_profile_picture)

    def test_profile_string_is_as_expected(self):
        """
        Checks if the profile's __str__ method returns the expected string
        """
        newUser = self.createTestUser()
        profile = newUser.profile
        expected_string = f"{newUser.username}'s (id: {newUser.pk}) profile"

        self.assertEqual(str(profile), expected_string)