from django.contrib import admin

# Register your models here.
from blog.models import BlogsPost,Favor


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

# class BlogsPostAdmin(admin.ModelAdmin):
#     def likesti(self):
#         return int(self.like)

admin.site.register(BlogsPost,BlogsPostAdmin)
admin.site.register(Favor)