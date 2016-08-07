from django.shortcuts import render
from .models import Post
from django.utils import timezone


def main_page(request):
    return render(request, 'blog/main_page.html', {})


def blog_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/blog_page.html', {"posts": posts})
