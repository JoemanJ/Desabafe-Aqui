from django.contrib.auth.models import User
def createTestUser(username="TestUser", email="test@user.com",
                    password="testPassword"):
    """ 
    Creates a sample new user
    """
    newUser = User.objects.create(username=username,
                                    email=email,
                                    password=password)
    return newUser