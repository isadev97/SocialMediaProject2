from django.shortcuts import render, redirect
from social_media_app.models import User, Post
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
        return render(request, "index.html", {"error": True, "msg" : "GET method not allowed"})    
    caption = request.POST['caption']
    post = Post.objects.create(
        user=request.user,
        caption=caption
    )
    return redirect("index")