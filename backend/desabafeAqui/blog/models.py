from django.db import models
from django.contrib.auth.models import User

import secrets
import string

def user_profile_picture_path(instance, filename) -> str:
    """ 
    Helper function to define the upload path  for user profile pictures.
    The default path is 'profile_pictures/[username's id].
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
                           help_text="Escreva um pouco sobre você",
                           db_comment="User's biografy")
    
    def __str__(self):
        return f"{self.user.username}'s (id: {self.user.pk}) profile"
    
    class Meta:
        ordering = ['user']
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"
    
class Post(models.Model):
    """
    A post made by a user.
    """
    author = models.ForeignKey(User, 
                             verbose_name=("The user that made the post"), 
                             on_delete=models.CASCADE,
                             )
    
    text = models.TextField("The text of the post",
                            max_length=5000,
                            null=False, blank=False,
                            help_text="Escreva aqui o que você quer desabafar",
                            db_comment="The text of the post")
    
    created_at = models.DateTimeField("Date the post was published",
                                          auto_now_add=True,
                                          help_text="Data de criação do desabafo",
                                          db_comment="Date the post was published")
    
    updated_at = models.DateTimeField("Date the post was last edited",
                                       auto_now=True,
                                       help_text="Data da última edição do desabafo",
                                       db_comment="Date the post was last edited")
    
    slug = models.SlugField(max_length=8, 
                            unique=True, 
                            blank=True,
                            db_comment="Unique, random, small id for the post")

    def __str__(self):
        return self.text
    
    def save(self, *args, **kwargs):
        """
        If the post doesn't have a slug yet, creates a random one before saving
        """
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        """
        Generates a unique 16-digit slug for the post
        """
        characters = string.ascii_letters + string.digits
        new_slug = ''.join(secrets.choice(characters) for _ in range(8))
        
        # Guard against duplicate slugs
        if Post.objects.filter(slug=new_slug).exists():
            return self.generate_unique_slug()
        
        return new_slug

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
