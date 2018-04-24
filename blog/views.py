from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailedView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'anything'
