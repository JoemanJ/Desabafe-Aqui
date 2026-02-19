from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

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