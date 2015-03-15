from django.contrib import admin
from blog.models import BlogsPost,Tag


admin.site.register(BlogsPost)
admin.site.register(Tag)