from django.db import models
from django.contrib.auth import get_user_model

# Post:
# userID(FK)(User)
# title
# content
# image
# create_time
# update_time

# Comment:
# postID(FK)(Post)
# userID(FK)(User)
# content
# create_time
# update_time

User = get_user_model()

# Create your models here.

class Post(models.Model):
    writer = models.ForeignKey(to= User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=64)
    bio = models.TextField(verbose_name='자기소개', blank=True)
    profile_photo = models.ImageField(blank=True)
    