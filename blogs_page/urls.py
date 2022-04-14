from django.urls import path

from .views import BlogsListView, BlogsDetailView

urlpatterns = [
    path('', BlogsListView.as_view(), name="blog_list"),
    path('<uuid:pk>/', BlogsDetailView.as_view(), name='blog_detail'),
]