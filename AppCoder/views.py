

from datetime import datetime
from importlib.metadata import requires
import profile
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 

from django.shortcuts import redirect
from django.urls import reverse_lazy

from AppCoder.forms import  ContactForm, PostForm, PostEditForm,EditarPerfil
from AppCoder.models import  Post,ImagenDePerfil

##Nuevas Imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def inicio(request):
    imagenes= ImagenDePerfil.objects.filter(user=request.user.id)
    return render(request, "AppCoder/inicio.html",{"url":imagenes[0].imagen.url})

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
    
    
######Perfil

class UserProfile(LoginRequiredMixin, ListView):
    model= User
    template_name = 'AppCoder/profile.html'
    context_object_name = 'profile'
    
@login_required
def perfilEdit(request):
    profile = request.user

    if request.method == 'POST':
        formulario = EditarPerfil(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            profile.first_name = data['first_name'] 
            profile.email = data['email']
            profile.set_password(data['password1'])
            profile.save()
            return redirect('post')
    else:
        formulario = EditarPerfil({'email': profile.email})
    
    return render(request, 'AppCoder/profile.html', {'form': formulario})