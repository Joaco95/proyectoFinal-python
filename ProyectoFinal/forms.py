from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, CharField, PasswordInput




class RegistroDeUsuarios(UserCreationForm):

    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repetir Contraseña', widget=PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
