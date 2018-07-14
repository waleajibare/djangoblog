from django.urls import path

from posts import views
from posts.views import PostDetailView

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('post/<pk>/', PostDetailView.as_view(), name='detail'),
    #path('<int:post_id>/', views.detail, name='detail'),
    #path('post/', create_post, name='create_posts'),
    #path('post/update/<int:id>/', update_post, name='update_post'),
    #path('post/delete/<int:id>/', delete_post, name='delete_post'),
    #path('post/create', create_posts, name='create_posts'),

]