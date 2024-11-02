from rest_framework import generics
from .models import Post, BannerImage
from .serializers import PostSerializer, BannerImageSerializer

# List view for all posts
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Detail view for a single post
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# List view for all banner images
class BannerImageListView(generics.ListAPIView):
    queryset = BannerImage.objects.all()
    serializer_class = BannerImageSerializer
