from django.contrib import admin
from .models import BlogModel


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'blog_content']


admin.site.register(BlogModel, BlogAdmin)
