from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    caption = models.TextField(default="")
    image = models.ImageField(null=True, upload_to='profile_images')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "profile"


class Post(models.Model):
    user = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    caption = models.TextField(default="")
    image = models.ImageField(null=True, upload_to='post_images')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "post"
        

class LikePost(models.Model):
    user = models.ForeignKey(User, related_name='like_post', on_delete=models.CASCADE) # user_id to use id directly
    post = models.ForeignKey(Post, related_name='like_post', on_delete=models.CASCADE) # post_id to use id directly
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "like_post"
    
    