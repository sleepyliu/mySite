from django.contrib import admin
from blog.models import BlogsPost


class BlogsPostAdmin(admin.ModelAdmin):
    """docstring for BlogsPostAdmin"""
    fieldsets = [
        ('Title',            {'fields': ['title']}),
        ('Content',          {'fields': ['body'], 'classes': ['collapse']}),
        ('Date information', {'fields': ['timestamp']}),
        ('Votes',            {'fields': ['votes']}),
    ]

    list_display = ('title','timestamp')
    list_filter = ['timestamp']
    search_fields = ['Title']

admin.site.register(BlogsPost,BlogsPostAdmin)

