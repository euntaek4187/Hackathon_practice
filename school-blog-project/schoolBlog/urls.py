from django.urls import path
from . import views

app_name = 'schoolBlog'

urlpatterns = [
    path('', views.index, name='index'),
]
