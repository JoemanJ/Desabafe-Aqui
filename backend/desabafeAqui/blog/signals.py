from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    """
    Callback function that automatically creates a profile once a user is
    created, and makes sure the profile is saved along with the user
    
    :param sender: The User model class
    :param instance: The newly created/saved User instance
    :param created: True if the user was just created, false if a previously
    created user was saved.
    :param kwargs: ...
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()