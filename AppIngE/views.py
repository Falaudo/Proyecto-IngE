from multiprocessing import context
from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
# Creación de usuario
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario=form.cleaned_data['usuario']
            contrasena=form.cleaned_data['contrasena1']
        form.save()
        return render(request, "home.html",{"mensaje":"Usuario creado"})
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form":form})

# inicio de sesión
def login_request(request):

    if request.method == "POST":
        form=AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contrasena=form.cleaned_data.get('password1')
            user = authenticate(username=usuario, password=contrasena)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render (request, "login.html", {"mensaje": "Los datos ingresados son incorrectos"} )
        else: 
                return render (request,"login.html", {"mensaje": "Formulario erróneo. Por favor, intentelo nuevamente."})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {'form':form})

@login_required
def logout_request(request):
    logout(request)
    return redirect('ingresar')

#Edición de perfil
@login_required
def editarPerfil(request):

    usuario = request.usuario

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:

            informacion=miFormulario.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "profile.html")
    else:
        miFormulario = UserEditForm(initial={ 'email': usuario.email})

    return render(request, "editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

# Perfil
@login_required
def perfil(request):
    usuario=request.user
    return render(request, 'profile.html',{'usuario':usuario,'imagen':inicio(request), 'posteos': Post(request)  })

def Post(request):
    posteos=Posteo.objects.filter(autor=request.user)
    if len(posteos) != 0:
        posteo=posteos
    else:
        posteo=0
    return posteo

#Avatar
@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid: 
            u=User.objects.get(usuario=request.user)
            avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'profile.html')

    else:
        miFormulario= AvatarFormulario()
    return render(request, "agregarAvatar.html",{"miFormulario":miFormulario})


def inicio(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    return render(request,"home.html",{"url":avatares[0].imagen.url})

# About
def about(request):
    return render(request, 'about.html')

#Posteos

# Lista de Posts en el inicio.

class ListaPosts(generic.ListView):
    queryset = Posteo.objects.all().order_by('creacion')
    template_name = 'home.html'

# Detalle Posts

class DetallePosts(generic.DetailView):
    model = Posteo
    template_name = 'DetallePosts.html'

# Crear Posteos
class CrearPosteos(LoginRequiredMixin, generic.CreateView):
    def get(self, request, *args, **kwargs):
        context= {'miFormulario': CrearPosteoForm()}
        return render(request, 'posts.html', context)
    
    def posteos(self, request, *args, **kwargs):
        miFormulario= CrearPosteoForm(request.POST, request.FILES)
        if miFormulario.is_valid():
            posteo=miFormulario.save(commit=False)
            posteo.autor=self.request.user
            slug= posteo.titulo
            posteo.slug=slug.replace(' ', '_').lower()
            posteo.save()
            return redirect (reverse_lazy('DetallePosts',args= [posteo.slug]))
        return render(request, 'posts.html',{'miFormulario': miFormulario })

#Actualización del post
class ActualizarPosteos(generic.UpdateView):
    model = Posteo
    fields = ['titulo', 'subtitulo', 'imagen', 'contenido']
    labels = { "titulo": "Título", "subtitulo":"Subtítulo", "imagen":"Imagen", "contenido": "Contenido"}
    template_name = 'atualizacionPosteo.html'

  
#Eliminar el post
class BorrarPosteos(generic.DeleteView):
    model = Posteo
    success_url = reverse_lazy('home')
    template_name = "borrarPosteo.html"

   