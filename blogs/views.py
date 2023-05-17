from django.shortcuts import render
from .models import BlogModel
from django.views.generic import ListView, DetailView


class BlogListView(ListView):
    template_name = 'blog.html'
    queryset = BlogModel.objects.all()


class BlogDetailView(DetailView):
    template_name = 'blog-details.html'
    model = BlogModel