

from datetime import datetime
# from tkinter.tix import Form
from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.views.generic import ListView

from django.shortcuts import redirect
from AppCoder.forms import reseñasForm
from AppCoder.models import reseñas

from AppCoder.forms import RegistroForm, ContactForm
from AppCoder.models import reseñas,Registro



def inicio(request):
    return render(request, "AppCoder/inicio.html")
#######################################################################################################
##ATENCION##
##VIEW DE JOAQUIN
##VIEW para utilizar con forms.py (no funciona),la funcion de abajo si funciona


def registro(request):
    if request.method == 'POST':
        formularioRegistro=RegistroForm(request.POST)
        if formularioRegistro.is_valid():
            dataRegistro=formularioRegistro.cleaned_data
            Registro.objects.create(nombreRegis=dataRegistro['Nombre'],emailRegis=dataRegistro['Email'],fechaDeNacimientoRegis=dataRegistro['Fecha'])
            return redirect('usuarios')
    else:
        formularioRegistro=RegistroForm()
    return render(request, "AppCoder/registro.html",{'formularioRegistro':formularioRegistro})
#########################################################################################################
""" def registro(request):
    if request.method == 'POST':
        Nombre=request.POST['Nombre']
        Email=request.POST['Email']
        FechaDeNacimiento=request.POST['FechaDeNacimiento']
        print(request.POST)
        print(Registro.objects.all())
        Registro.objects.create(nombreRegis=Nombre,emailRegis=Email,fechaDeNacimientoRegis=FechaDeNacimiento)
        #return render(request, "AppCoder/usuarios.html")
        return redirect('usuarios')
    return render(request, "AppCoder/registro.html") """

###############################################################################################################
def Usuarios(request):
    return render(request, "AppCoder/usuarios.html",{'usuarios':Registro.objects.all()})
    
#def busquedaUsuarios(request):
#    busqueda=f"Usuario es: {request.GET['Nombre']}"
#    return HttpResponse(busqueda)

def busquedaUsuarios(request):
    if request.GET["Email"]:
        email=request.GET["Email"]
        #registro=Registro.objects.filter(emailRegis__icontains=email)
        registro=Registro.objects.filter(emailRegis=email)
        return render(request,"Appcoder/busqueda.html", {"registro":registro,"email":email})

    #busqueda=f"Usuario es: {request.GET['Email']}"
    #return HttpResponse(busqueda)


###############################################################################################################

########## JEREMIAS ##############
def contacto(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        person_name = request.POST['nombre']
        success_message = f'Gracias por comunicarte con nosotros {person_name}. Te responderemos a la brevedad vía email.'
        if contact_form.is_valid():
            contact_form.cleaned_data
            return render(request, 'AppCoder/contacto.html', {'contact_form':ContactForm,'success_message':success_message, 'person_name': person_name})
    else:
            return render(request, 'AppCoder/contacto.html', {'contact_form':ContactForm})
        

def discos(request):
    return render(request, "AppCoder/discos.html")

########## JESUS ##############
# Con el uso de POST podemos guardar los datos ingresados en el formulario, fijar su fecha y guardar todo en la base de datos.
    
def reseñas(request):
    form = reseñasForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.fecha = datetime.now()
            message.save()
            return redirect("reseñas")
    else:
        return render(request, "AppCoder/reseñas.html", {"form": form})

 
 
class reseñasListView(ListView):
#Renderizamos la pagina 
    model = reseñas
    def get_context_data(self, **kwargs):
        context = super(reseñasListView, self).get_context_data(**kwargs)
        return context 
 

###############################################################################################################
  
 