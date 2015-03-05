from django.contrib import admin

# Register your models here.
from blog.models import BlogsPost


class BlogsPostAdmin(admin.ModelAdmin):
    # fields = ['title', 'timestamp']
    fieldsets = [
        ('Title',            {'fields': ['title']}),
        ('Content',          {'fields': ['body'], 'classes': ['collapse']}),
        ('Date information', {'fields': ['timestamp']}),
    ]

    list_display = ('title','timestamp')
    list_filter = ['timestamp']
    search_fields = ['Title']

admin.site.register(BlogsPost,BlogsPostAdmin)