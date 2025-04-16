from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import BlogPost
from .forms import BlogPostForm  # Import the BlogPostForm

# Blog Views
def frontpage(request):
    return render(request, 'blog/frontpage.html')

def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

from django.shortcuts import render, redirect
from .forms import BlogPostForm  # Make sure this form exists

def post_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            return render(request, 'blog/post_blog.html', {'form': BlogPostForm(), 'latest_post': blog})
    else:
        form = BlogPostForm()

    return render(request, 'blog/post_blog.html', {'form': form})

# User Authentication Views
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')  # redirect after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('frontpage')  # redirect after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # redirect after logout
