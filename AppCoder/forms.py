
import email
from django.forms import Form, CharField, IntegerField, EmailField,DateField
from django import forms

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
from AppCoder.models import reseñas, Post

class reseñasForm(forms.ModelForm):
    class Meta:
        model = reseñas
        fields = ("mensaje",)   # NOTE: the trailing comma is required
        
        
### Jeremías
class ContactForm(Form):
  nombre = CharField()
  email = EmailField()
  asunto = CharField()
  mensaje = CharField()
  
class PostForm(forms.ModelForm):
  class Meta:
    model= Post
    fields= ('title', 'author', 'body',)
    
    widgets = {
      
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'author': forms.TextInput(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      
    }
    
class PostEditForm(forms.ModelForm):
  class Meta:
    model= Post
    fields= ('title', 'body',)
    
    widgets = {
      
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      
    }
  
        


    
