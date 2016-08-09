from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm, AuthForm


def need_authentication(func):
    def f(request, *args, **kwargs):
        if not isinstance(request.user, User):
            return redirect("auth")
        return func(request, *args, **kwargs)
    return f


def blog_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/blog_page.html', {"posts": posts})


def post_detail(request, pk):
    post = [get_object_or_404(Post, pk=pk)]
    return render(request, "blog/blog_page.html", {"posts": post})


@need_authentication
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'edit': False})


@need_authentication
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("post_detail", pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'edit': True})


@need_authentication
def post_delete(request, pk):
    Post.objects.filter(pk=pk).delete()
    return redirect('blog_page')


def auth(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user = authenticate(username=user.last_name, password=user.password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect("blog_page")
    form = AuthForm()
    return render(request, 'blog/auth.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user = User.objects.create_user(user.last_name, password=user.password)
            login(request, user)
            return redirect("blog_page")
    form = AuthForm()
    return render(request, 'blog/registration.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect("blog_page")
