#PARA EL LOGIN
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


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
                return  redirect('inicio')
        
            else:
                return render(request,'login.html',
                              {'form': form,
                               'error': 'No es valido el usuario y contraseña'})
        
        else:
            return render(request,'login.html', {'form':form})
    
    form = AuthenticationForm()
    
    return render(request, "login.html", {'form':form}) #Si es incorrecto se queda en el Login

#JESUS 16/02

def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
        
            username = form.cleaned_data['username']
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form":form})

#Jeremías: actualicé los render para que dirijan a las páginas que correponden. 18/02
#Jeremías: LOGOUT. 18/02

def logout_user(request):
    logout(request)
    messages.success(request, ('Has cerrado sesión'))
    return redirect('post')


