from django.shortcuts import render, redirect
from social_media_app.models import User, Post, LikePost, Profile
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='sign_in')
def index_view(request):
    data = {
        "post_list" : Post.objects.all() if request.user.is_authenticated else []
    }
    return render(request, "index.html", data)

def sign_up_view(request):
    page_name= "signup.html"
    if request.method == "POST":
        # logic to create the user 
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not username:
            return render(request, page_name, {"error": True, "msg" : "Username is required"})
        if not email:
            return render(request, page_name, {"error": True, "msg" : "Email is required"})
        if not password:
            return render(request, page_name, {"error": True, "msg" : "Password is required"})
        if User.objects.filter(username=username).exists():
            return render(request, page_name, {"error": True, "msg" : "This username already exists"})
        if User.objects.filter(email=email).exists():
            return render(request, page_name, {"error": True, "msg" : "This email already exists"})
        User.objects.create_user(username=username, email=email, password=password)
        user = auth.authenticate(username=username, password=password)
        if user:
            Profile.objects.get_or_create(user=user)
            auth.login(request, user)
            return redirect("index")
        else:
            return render(request, page_name, {"error": True, "msg" : "Authentication could not happen"})
    else: 
        # GET Method render the page
        return render(request, page_name)

def sign_in_view(request):
    page_name = "signin.html"
    if request.method == "POST":
        # sign in logic
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            Profile.objects.get_or_create(user=user)
            auth.login(request, user)
            return redirect("index")
        else:
            return render(request, page_name, {"error": True, "msg" : "Authentication could not happen"})
    else: 
        # GET Method render the page
        return render(request, page_name)

@login_required(login_url='sign_in')
def sign_out_view(request):
    auth.logout(request)
    return redirect("index")

@login_required(login_url='sign_in')
def create_post_view(request):
    if request.method == 'GET':
        return redirect("index")  
    caption = request.POST['caption']
    image = request.FILES.get('post_image', None)
    Post.objects.create(
        user=request.user,
        caption=caption,
        image=image
    )
    return redirect("index")

@login_required(login_url='sign_in')
def like_post_view(request, post_id):
    if request.method == 'GET':
        return redirect("index")
    # post_id = request.POST['post_id']
    print(request.POST)
    print(request.POST['tmp_id'])
    LikePost.objects.create(
        user=request.user,
        post_id=post_id
    )
    return redirect("index")

@login_required(login_url='sign_in')
def my_profile_view(request):
    page_name = "profile.html"
    if request.method == 'POST':
        return redirect("index")
    qs = LikePost.objects.filter(post__user=request.user)
    print(qs.query)
    data = {
        "number_of_posts_made_by_user" : request.user.post.all().count(), # or Post.objects.filter(user=request.user).count()
        "number_of_likes_made_by_user": request.user.like_post.all().count(), # or LikePost.objects.filter(user=request.user).count()
        "number_of_likes_received_for_user" : qs.count(),
        "profile_image": request.user.profile.image
    }
    return render(request, page_name, context=data)

@login_required(login_url='sign_in')
def upload_profile_image(request):
    if request.method == 'GET':
        return redirect("index")
    image = request.FILES.get('profile_image', None)
    profile = request.user.profile
    profile.image = image 
    profile.save()
    return redirect("my_profile")
    
    
    


