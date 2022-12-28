from django.urls import path
from . import views

app_name = 'Blog_App'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),

]