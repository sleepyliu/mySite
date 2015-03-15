from django import forms
from .models import BlogsPost,Tag
 
class PostForm(forms.ModelForm):
    """docstring for PostForm"""
    class Meta:
        model = BlogsPost
        fields = ('title', 'body')


class TagForm(forms.ModelForm):
    """docstring for TagForm"""
    class Meta:
        model = Tag
        fields = ('tag_name',)


        