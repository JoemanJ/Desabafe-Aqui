from django.contrib import admin
from .models import UserProfile, Post, Comment

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'bio')
    search_fields = ('user__username',)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'author', 'text', 'created_at', 'updated_at')
    readonly_fields = ('slug')
    search_fields = ('slug', 'author__username', 'text')
    list_filter = ('created_at', 'author__username')

    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'text')
    search_fields = ('text', 'author__username', 'post__slug')