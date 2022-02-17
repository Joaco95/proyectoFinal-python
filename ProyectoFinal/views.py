#PARA EL LOGIN
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


#JESUS 15/02

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password =contra)
        
            if user is not None:
                login(request, user)
                return HttpResponse(f'Sesion del Usuario {user} iniciada correctamente')
        
            else:
                return render(request,'AppCoder/login.html',
                              {'form': form,
                               'error': 'No es valido el usuario y contraseña'})
        
        else:
            return render(request,'AppCoder/login.html', {'form':form})
    form = AuthenticationForm()
    return render(request, "AppCoder/login.html", {'form':form}) #Si es incorrecto se queda en el Login

#JESUS 16/02

def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #form = UserRegisterForm(request.POST)
        
        if form.is_valid():
        
            username = form.cleaned_data['username']
            form.save()
            return HttpResponse(f' Usuario {username} creado correctamente')
    
    else:
        form = UserCreationForm()
        #form = UserRegisterForm()
    return render(request, "AppCoder/signup.html", {"form":form})



