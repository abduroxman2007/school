from django.db import models

class Pictures(models.Model):
    img = models.ImageField(upload_to="post_images/")

    def __str__(self):
        return f"{self.id} - {self.img}"

class Post(models.Model):
    image = models.ImageField(upload_to='post_images/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    pictures = models.ManyToManyField(Pictures, related_name="posts")

    def __str__(self):
        return self.title



class BannerImage(models.Model):
    image = models.ImageField(upload_to='banner_images/')

    def __str__(self):
        return f"Banner Image {self.id}"
