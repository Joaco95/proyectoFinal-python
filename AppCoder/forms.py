
import email
from django.forms import Form, CharField, IntegerField, EmailField,DateField

class RegistroForm(Form):
  Nombre=CharField()
  Email=EmailField()
  Fecha=DateField()

#class ReseñasForm(Form):
 #   Mensaje = CharField()
  #  Email = IntegerField() '''

#class ProfesorForm(Form):
    # Con las vistas basadas en clases no hace falta!
 #   nombre = CharField(max_length=30)
  #  apellido = CharField(max_length=30)
   # email = EmailField()
    #profesion = CharField(max_length=30)
    
    
from django import forms
from AppCoder.models import reseñas

class reseñasForm(forms.ModelForm):
    class Meta:
        model = reseñas
        fields = ("mensaje",)   # NOTE: the trailing comma is required
        
        
### ContactForm por Jeremías
class ContactForm(Form):
  nombre = CharField()
  email = EmailField()
  asunto = CharField()
  mensaje = CharField()
  
        


    
