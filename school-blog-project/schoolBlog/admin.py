from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id','writer', 'title', 'content', 'image', 'created_at', 'updated_at')

admin.site.register(Comment)