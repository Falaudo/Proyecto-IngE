from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse


#Avatar
class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank= True)


#Posteos
class Posteo(models.Model):
    titulo= models.CharField(max_length=500, unique=True)
    slug=models.SlugField(max_length=500, unique=True)
    subtitulo=models.CharField(max_length=500)
    imagen=models.ImageField(upload_to='Imagen', null=True, blank=True)
    contenido=RichTextField()
    autor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='posteos')
    actualizacion=models.DateTimeField(auto_now=True)
    creacion=models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        ordering = ['-creacion']

    def get_absolute_url(self):
        return reverse('DetallePosteo', kwargs={'slug':self.slug})
    
    def __str__(self):
        return self.titulo


