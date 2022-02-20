
import email
from django.forms import Form, CharField, IntegerField, EmailField,DateField, PasswordInput
from django import forms
from AppCoder.models import  Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

        
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
    username = CharField()
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repetir Contraseña', widget=PasswordInput)

    class Meta:
        model = User
        fields = [ 'username','email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

    
