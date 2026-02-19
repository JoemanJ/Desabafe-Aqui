from django.db import models
from django.contrib.auth.models import User

import secrets
import string

config = {
    "POST_SLUG_SIZE": 8
}

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
                                help_text="A imagem que aparece junto com seus posts",
                                )
    bio = models.TextField("User's biography",
                           blank=True,
                           max_length=1000,
                           help_text="Escreva um pouco sobre você")
    
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
                               related_name="posts",
                               on_delete=models.CASCADE)
    
    text = models.TextField("The text of the post",
                            max_length=5000,
                            null=False, blank=False,
                            help_text="Escreva aqui o que você quer desabafar")
    
    created_at = models.DateTimeField("Date the post was published",
                                          auto_now_add=True,
                                          help_text="Data de criação do desabafo")
    
    updated_at = models.DateTimeField("Date the post was last edited",
                                       auto_now=True,
                                       help_text="Data da última edição do desabafo")
    
    slug = models.SlugField(max_length=8, 
                            unique=True, 
                            blank=True)

    def __str__(self):
        return f"{self.author.username}: {self.text[:20]}..."
    
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
        new_slug = ''.join(secrets.choice(characters) for _ in range(config["POST_SLUG_SIZE"]))
        
        # Guard against duplicate slugs
        if Post.objects.filter(slug=new_slug).exists():
            return self.generate_unique_slug()
        
        return new_slug

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
class Comment(models.Model):
    """
    A comment made by a user in a post
    """
    author = models.ForeignKey(User, 
                               verbose_name=("Author of the comment"), 
                               related_name="comments",
                               on_delete=models.CASCADE)
    
    post = models.ForeignKey(Post,
                             verbose_name=("Post the comment was made on"),
                             related_name="comments",
                             on_delete=models.CASCADE)
    
    text = models.TextField("Text of the comment",
                            max_length=500,
                            null=False, blank=False,
                            help_text="Escreva aqui o que você quer desabafar")
    
    created_at = models.DateTimeField("Date the comment was made",
                                      auto_now_add=True,
                                      help_text="Data de criação do comentário")
    
    updated_at = models.DateTimeField("Date the comment was last edited",
                                       auto_now=True,
                                       help_text="Data da última edição do comentário")
    
    def __str__(self):
        return f"{self.author} on {self.post.slug}: {self.text[:20]}"