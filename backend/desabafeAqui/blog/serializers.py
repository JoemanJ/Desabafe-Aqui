from rest_framework import serializers
from .models import UserProfile, Post, Comment

class UserProfileMiniSerializer(serializers.ModelSerializer):
    """
    Small user profile serializer that returns only the username and the profile
    picture. Useful to render authors of posts and comments.
    """
    username = serializers.ReadOnlyField(source='user.username')
    http_method_names = ['get']

    class Meta:
        model = UserProfile
        fields = ['username', 'picture']

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Full user profile serializer that returns username, profile picture and bio.
    If you don't need the bio, see UserProfileMiniSerializer.
    """
    username = serializers.ReadOnlyField(source='user.username')
    http_method_names = ['get', 'patch', 'head', 'options']

    class Meta:
        model = UserProfile
        fields = ['username', 'picture', 'bio']

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for posts. Returns text, slug, creation date and author's
    username and profile picture.
    """
    author_details = UserProfileMiniSerializer(source='author.profile', read_only=True)

    class Meta:
        model = Post
        fields = ['author_details', 'text', 'slug', 'created_at']
        read_only_fields = ['slug', 'created_at']        

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for comments. Returns author's username and the post's slug,
    text and creation date.
    """
    author_details = UserProfileMiniSerializer(source='author.profile', read_only=True)
    post = serializers.SlugRelatedField(slug_field='slug',
                                        queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['author_details', 'post', 'text', 'created_at']