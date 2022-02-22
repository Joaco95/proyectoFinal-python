
import email
from django.forms import Form, CharField, IntegerField, EmailField,DateField, PasswordInput,ImageField
from django import forms
from AppCoder.models import  Post,Perfiles
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

        
### Jeremías
  
class PostForm(forms.ModelForm):
  class Meta:
    model= Post
    fields= ('title', 'author', 'body', 'header_image',)
    
    widgets = {
      
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'user', 'type':'hidden'}),
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
  
        
class EditarPerfil(UserCreationForm):
    
    first_name = CharField()
   
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repetir Contraseña', widget=PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

    
class EditarDescripcion(forms.ModelForm):
  class Meta:
    model= Perfiles
    fields= ('descripcion', 'link', 'image')
    
    widgets = {
      
      'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
      'link': forms.Textarea(attrs={'class': 'form-control'}),
      
      
    }
   
class EditarImagen(Form):
    imagen = ImageField(required=True)