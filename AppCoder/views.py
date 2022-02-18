

from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from AppCoder.forms import  ContactForm, PostForm, PostEditForm
from AppCoder.models import  Post



def inicio(request):
    return render(request, "AppCoder/inicio.html")
    

###############################################################################################################

    
#JEREMIAS

class PostView(ListView):
    model = Post
    template_name = "AppCoder/post.html"
    ordering = ['-date']
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = "AppCoder/article_details.html"
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "AppCoder/add_post.html"
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = "AppCoder/edit_post.html"
    form_class = PostEditForm
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "AppCoder/delete_post.html"
    success_url = reverse_lazy('post')
    
