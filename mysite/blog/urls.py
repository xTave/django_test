from django.conf.urls import url
from django.contrib import auth
from . import views

urlpatterns = [
    url(r'^$', views.blog_page, name="blog_page"),
    url(r'^auth/', views.auth, name='auth'),
    url(r'^logout/', views.log_out, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name="post_delete")
]