from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import BlogPost
from itertools import chain


class HomeView(ListView):
    model = BlogPost
    template_name = "blog/blog_base.html"
    paginate_by = 2


class ViewPage(DetailView):
    model = BlogPost
    template_name = "blog/view_page.html"
    context_object_name = "blog"


class PostTetail(DetailView):
    model = BlogPost
    template_name = "blog/post_detail.html"
    context_object_name = "blog"
