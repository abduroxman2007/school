from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='post_images/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class BannerImage(models.Model):
    image = models.ImageField(upload_to='banner_images/')

    def __str__(self):
        return f"Banner Image {self.id}"
