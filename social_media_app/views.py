from django.shortcuts import render

# Create your views here.
def index_view(request):
    print(request.user)
    return render(request, "index.html")

def sign_up_view(request):
    return render(request, "signup.html")

def sign_in_view(request):
    return render(request, "signin.html")