from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)