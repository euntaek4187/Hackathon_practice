
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from schoolBlog.views import test, index, detail, delete, update, comment, comment_delete

from django.contrib.auth.views import LogoutView

from schoolBlog.views import ProfileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('<int:id>/', detail, name='post-detail'),
    path('<int:id>/delete/', delete, name='post-delete'),
    path('<int:id>/edit/', update , name='post-update'),
    path('<int:id>/comment/', comment, name='post-comment'),
    path('<int:post_id>/comment/delete/<int:comment_id>/', comment_delete, name='post-comment-delete'),

    path('accounts/', include('accounts.urls')),
    path('schoolBlog/', include('schoolBlog.urls')),
     path('logout/', LogoutView.as_view(), name='logout'),
    

    path('profile/<int:pk>/', ProfileView.as_view(), name='schoolBlog:profile'),
    path('admin/', admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
