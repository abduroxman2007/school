# content/serializers.py
from rest_framework import serializers
from .models import *

class Pictures(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = ["img"]
class PostSerializer(serializers.ModelSerializer):
    pictures = Pictures(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'image', 'title', 'description', 'date', 'pictures']

class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ['id', 'image']
