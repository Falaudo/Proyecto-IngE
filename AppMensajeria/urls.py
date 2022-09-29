from django.urls import path
from .views import *

urlpatterns = [
    path('', mensajeria, name='mensajeria'),
    path('enviar/', EnviarMensaje.as_view(), name='enviar'),
    path('enviado/', enviado, name='enviado'),   
]