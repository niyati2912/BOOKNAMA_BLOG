from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'content', 'cover_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter blog title',
                'class': 'form-control'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your blog content here...',
                'class': 'form-control',
                'rows': 6
            }),
        }