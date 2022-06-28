from django.shortcuts import render
from django.db import models
from .models import Post
import blog
from django.urls import reverse_lazy
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

class PostListView (ListView):
    model = Post
    template_name = 'post_list.html'
    # success_url ="/"
  

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post
    field = "__all__"
    template_name= 'blog/post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy("blog:all")



