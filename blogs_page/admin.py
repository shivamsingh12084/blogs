from django.contrib import admin

from .models import Blogs
# Register your models here.
class BlogsAdmin(admin.ModelAdmin):
    """Here I have provided the representation of blogs model in django admin"""
    list_display = ("title", "author", "created_at")


admin.site.register(Blogs, BlogsAdmin)