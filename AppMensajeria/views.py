from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import MensajeForm
from .models import Mensaje
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


#Mostrar mensajes recibidos 
@login_required
def mensajeria(request):
    return render(request, 'mensajeria.html', {'mensajes': obtenerMensajesRecibidos(request)})


def obtenerMensajesRecibidos(request):
    mensajes = Mensaje.objects.filter(para=request.user)
    if len(mensajes) != 0:
        mensaje= mensajes.order_by('-creacion')
    else:
        mensaje = 0
    return mensaje

#Enviar mensajes
class EnviarMensaje(LoginRequiredMixin, generic.CreateView):
    def get(self, request, *args, **kwargs):
        context = {'miFormulario': MensajeForm()}
        return render(request, 'enviado.html', context)

    def posteo(self, request, *args, **kwargs):
        miFormulario = MensajeForm(request.POST)
        if miFormulario.is_valid():
            posteos = miFormulario.save(commit=False)
            posteos.sender = self.request.user
            posteos.save()
            return redirect(reverse_lazy('enviado'))
        return render(request, 'enviado.html', {'miFormulario': miFormulario})


#Mostrar mensajes enviados
@login_required
def enviado(request):
    return render(request, 'enviado.html', {'mensajes': obtenerMensajesEnviados(request)})

def obtenerMensajesEnviados(request):
    mensajes = Mensaje.objects.filter(de=request.user)
    if len(mensajes) != 0:
        mensaje = mensajes.order_by('-creacion')
    else:
        mensaje = 0
    return mensaje


