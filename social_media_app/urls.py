from django.urls import path
from social_media_app.views import (
    index_view, 
    sign_up_view, 
    sign_in_view, 
    sign_out_view, 
    create_post_view,
    like_post_view,
    my_profile_view,
    upload_profile_image
)

urlpatterns = [
    path('', index_view, name="index"),
    path('sign-up/', sign_up_view, name="sign_up"),
    path('sign-in/', sign_in_view, name="sign_in"),
    path('sign-out/', sign_out_view, name="sign_out"),
    path('create-post/', create_post_view, name="create_post"),
    path('like-post/<int:post_id>/', like_post_view, name="like_post"),
    path('my-profile/', my_profile_view, name="my_profile"),
    path('upload-profile-image/', upload_profile_image, name="upload_profile_image")
    
]