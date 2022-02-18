
import email
from django.forms import Form, CharField, IntegerField, EmailField,DateField
from django import forms
from AppCoder.models import  Post
        
        
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
  
        


    
