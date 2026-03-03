from rest_framework import viewsets, permissions, mixins
from .models import (Post, 
                     Comment, 
                     UserProfile)
from .serializers import (PostSerializer,
                          CommentSerializer, 
                          UserProfileSerializer,
                          UserProfileMiniSerializer)
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    """
    Provides automatic actions for:
    list (GET)
    create (POST)
    retrieve (GET single post)
    update (PUT/PATCH)
    destroy (DELETE)
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """
    Provides automatic actions for:
    list (GET)
    create (POST)
    retrieve (GET single post)
    update (PUT/PATCH)
    destroy (DELETE)
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ProfileViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
    Provides automatic actions for:
    list (GET)
    retrieve (GET single profile)
    update (PATCH)
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    lookup_field = 'user__username'

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class ProfileMiniViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides automatic actions for:
    list (GET)
    create (POST)
    retrieve (GET single MiniProfile (username and profile picture only))
    update (PUT/PATCH)
    destroy (DELETE)
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileMiniSerializer

    lookup_field = 'user__username'

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]