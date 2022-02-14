from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Model
from django.utils import timezone

from django.utils import timezone

from django.db.models.fields import (
    BooleanField, CharField, DateField, EmailField, IntegerField,
    GenericIPAddressField, URLField, DecimalField, TimeField
)

''' class reseñas(models.Model):
    Mensaje = models.CharField(max_length=300)
    Email = models.EmailField(max_length=300)
    Fecha = models.DateTimeField("date logged") 
     '''
    
###Lo hizo Jesus
class reseñas(models.Model):
    mensaje = models.CharField(max_length=300)
    fecha = models.DateTimeField("date logged")

    def __str__(self):
        date = timezone.localtime(self.fecha)
        return f"'{self.mensaje}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

  
###Lo hizo Joaquin
class Registro(models.Model):
    nombreRegis = models.CharField(max_length=300)
    emailRegis = models.EmailField(max_length=300)
    fechaDeNacimientoRegis = models.DateField() 
    
    def __str__(self):
        return f""" Nombre de Usuario:  {self.nombreRegis}- 
                    Email:  {self.emailRegis}-
                    Fecha de naciemiento:  ({self.fechaDeNacimientoRegis})-
                    Bienvenido  {self.nombreRegis}"""

class Post(models.Model):
    title=models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    body = models.TextField()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)