

from datetime import datetime
from email.mime import image
from importlib.metadata import requires
import profile
from pyexpat import model
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 

from django.shortcuts import redirect
from django.urls import reverse_lazy

from AppCoder.forms import  PostForm, PostEditForm,EditarPerfil,EditarDescripcion,EditarImagen
from AppCoder.models import  Post,Image,Perfiles

##Nuevas Imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



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
    
    
######Perfil##################

class UserProfile(LoginRequiredMixin, ListView):
    model= User
    template_name = 'AppCoder/profile.html'
    context_object_name = 'profile'
    
class EditProfile(UpdateView):
    model = Perfiles
    template_name = "AppCoder/imageProfile.html"
    form_class = EditarDescripcion
    success_url = reverse_lazy('miProfile')   

class EliminarUsuario(DeleteView):
    model= User
    template_name = "AppCoder/profile_confirm_delete.html"
    success_url = reverse_lazy('post')


@login_required
def editarContra(request):
    profile = request.user
    if request.method == 'POST':
        editar = EditarPerfil(request.POST)
        if editar.is_valid():
            data = editar.cleaned_data
             
            profile.first_name = data['first_name'] 
            
            profile.set_password(data['password1'])
            profile.save()
            return redirect('post')
    else:
        editar = EditarPerfil({'email': profile.email})
    
    return render(request, 'AppCoder/profile.html', {'usuarios': editar})


@login_required
def perfil(request):
    usuarios = User.objects.filter()
    avatares = Image.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'AppCoder/miProfile.html' , {'avatar_url': avatar_url, 'usuarios': usuarios})


@login_required
def editarImagen(request):
    if request.method == 'POST':
        formulario = EditarImagen(request.POST, request.FILES)

        if formulario.is_valid():
            avatar = Image(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return redirect('inicio')
    else:
        formulario = EditarImagen()

    return render(request, 'AppCoder/imagen.html', {'form': formulario})

@login_required
def editarDescripcion(request):

    if request.method == 'GET':
        usuarios = User.objects.filter()
        avatares = Image.objects.filter(user=request.user.id)
        formulario=EditarDescripcion(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Perfiles.objects.create(
                descripcion=data['descripcion'],
                link=data['link']
                )
            return redirect('miProfile')
        else:
            formulario = Perfiles()
        return render(request, 'AppCoder/imageProfile.html' , {'form': formulario, 'usuarios': usuarios})
    
    