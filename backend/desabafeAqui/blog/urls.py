from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (PostViewSet, 
                    CommentViewSet, 
                    ProfileViewSet,
                    ProfileMiniViewSet)

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('profile,', ProfileViewSet, 'profile')
router.register('profilemini', ProfileMiniViewSet, 'miniprofile')

urlpatterns = [
    path('', include(router.urls))
]
