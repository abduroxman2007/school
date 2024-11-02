from django.urls import path
from .views import PostListCreateView, PostDetailView, BannerImageListView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post_list_create'),      # List all posts, create new post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),       # Retrieve, update, delete a post
    path('banners/', BannerImageListView.as_view(), name='banner_list'),         # List all banner images
]
