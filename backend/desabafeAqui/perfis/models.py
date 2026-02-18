from django.db import models
from django.contrib.auth.models import User

def user_profile_picture_path(instance, filename) -> str:
    """ 
    Helper function to define the upload path  for user profile pictures.
    The default path is 'profile_pictures/[username].
    """
    return f"profile_pictures/{instance.user.pk}/{filename}"

class UserProfile(models.Model):
    """ Profile information about a user """
    user = models.OneToOneField(User,
                                verbose_name=("Owner of this profile"),
                                on_delete=models.CASCADE,
                                related_name="profile")

    picture = models.ImageField("User's profile picture",
                                upload_to=user_profile_picture_path,
                                blank=True,
                                db_comment="User's profile picture",
                                help_text="A imagem que aparece junto com seus posts",
                                )
    bio = models.TextField("User's biography",
                           blank=True,
                           max_length=1000,
                           help_text="Escreva um pouco sobre você")
    
    def __str__(self):
        return f"{self.user.username}'s (id: {self.user.pk}) profile"