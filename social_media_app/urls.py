from django.urls import path
from social_media_app.views import index_view, sign_up_view, sign_in_view, sign_out_view, create_post_view

urlpatterns = [
    path('', index_view, name="index"),
    path('sign-up/', sign_up_view, name="sign_up"),
    path('sign-in/', sign_in_view, name="sign_in"),
    path('sign-out/', sign_out_view, name="sign_out"),
    path('create-post/', create_post_view, name="create_post"),
]