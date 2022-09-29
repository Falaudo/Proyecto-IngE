from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Mensaje(models.Model):
    de = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="de")
    para = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="para")
    contenido = RichTextField()
    creacion = models.DateTimeField(auto_now=True)
