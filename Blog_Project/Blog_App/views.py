from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from Blog_App.models import Blog, Comment, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid #unique id generate
# Create your views here.

def blog_list(request):
    return render(request, 'Blog_App/blog_list.html', context={})


# BLOG CREATE
class CreateBlog(CreateView, LoginRequiredMixin):
    model = Blog
    template_name = 'Blog_App/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image')

    # non mentioned items generate
    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(' ', '-') + "-" + str(uuid.uuid4())










    