from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),               # Frontpage
    path('posts/', views.post_list, name='post_list'),          # Post List
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Post Detail

    # User Authentication URLs
    path('signup/', views.signup_view, name='signup'),          # Sign Up
    path('login/', views.login_view, name='login'),             # Log In
    path('logout/', views.logout_view, name='logout'),          # Log Out
]
