from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Creación de usuario

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email=forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2']
        help_text={k:"" for k in fields}

# Edición de usuario

class UserEditForm(UserCreationForm):
    username=forms.CharField(label='Modificar nombre de usuario')
    email=forms.EmailField(label="Modificar E-mail")
    password1=forms.CharField(label='Cambiar contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Modificar nombre')
    last_name = forms.CharField(label='Modificar apellido')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

#Avatar 
class AvatarFormulario(forms.Form):
    imagen=forms.ImageField(label="Imagen")

# Posteos

# -Crear posteos-

class CrearPosteoForm(forms.ModelForm):
    class Meta:
        model=Posteo
        fields=['titulo', 'subtitulo', 'imagen', 'contenido']
        labels={ "titulo":"Título", "subtitulo":"Subtítulo", "imagen":"Imagen", "contenido":"Contenido"}

# -Para postear una imagen-

class ImagenPosteoForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

