from django import forms
from .models import Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class AuthForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('last_name', 'password', )