from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id','writer', 'title', 'content', 'image', 'created_at', 'updated_at')

admin.site.register(Comment)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False   

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)