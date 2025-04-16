from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm
from django.utils import timezone

# Blog Views
def frontpage(request):
    return render(request, 'blog/frontpage.html')

@login_required(login_url='login')
def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required(login_url='login')
def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required(login_url='login')
def post_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.created_at = timezone.now()
            blog.save()
            return redirect('post_list')  # after posting, go to blog list
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
            return redirect('post_list')  # redirect after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')  # redirect after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # redirect after logout

@login_required(login_url='/login/')
def front_page(request):
    return render(request, 'front_page.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def front_page(request):
    return render(request, 'front_page.html')

def post_blog(request):
    return render(request, 'post_blog.html')