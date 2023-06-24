from django.contrib import admin
from social_media_app.models import User, Profile, Post, LikePost

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)

