from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blogs_page.models import Blogs

# Create your views here.
class BlogsListView(ListView):
    """Represents blogs list in template"""
    model = Blogs
    context_object_name = 'blog_list'
    template_name = "blogs/blog_list.html"


class BlogsDetailView(DetailView):
    """Represents details blogs list in template"""
    model = Blogs
    context_object_name = 'blog'
    template_name = "blogs/blogs_detail.html"