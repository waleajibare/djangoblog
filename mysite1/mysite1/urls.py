"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from posts import views as posts_views
from contact import views as contact_views
from posts.views import  PostDetailView
from posts.views import   create_posts
from posts.views import   update_post
from posts.views import   delete_post

urlpatterns = [
    path('posts/', include('posts.urls')),
    path('comments/', include('django_comments.urls')),
    path('accounts/', include('allauth.urls')),
    path('about/', posts_views.about, name='about'),
    path('profile/', posts_views.userProfile, name='profile'),
    path('privacy/', posts_views.privacy, name='privacy'),
    #path('contact/', posts_views.contact, name='contact'),
    path('terms/', posts_views.terms, name='terms'),
    path('contact/', contact_views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('', posts_views.home, name='home'),
    path('posts/create', create_posts, name='create_posts'),
    path('posts/update/<int:id>/', update_post, name='update_post'),
    path('posts/delete/<int:id>/', delete_post, name='delete_post'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)