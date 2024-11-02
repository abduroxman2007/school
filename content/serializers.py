# content/serializers.py
from rest_framework import serializers
from .models import Post, BannerImage

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'image', 'title', 'description', 'date']

class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ['id', 'image']
