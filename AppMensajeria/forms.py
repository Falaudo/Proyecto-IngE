from django import forms
from .models import *


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['para', 'contenido']
