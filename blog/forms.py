from django import forms
from .models import BlogsPost
 
class PostForm(forms.ModelForm):
    """docstring for PostForm"""
    class Meta:
        model = BlogsPost
        fields = ('title', 'body')

        