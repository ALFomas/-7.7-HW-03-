from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """class post form"""
    class Meta:
        model = Post
        fields = ['author',
                  'title',
                  'text',
                  'categories',
                  ]

