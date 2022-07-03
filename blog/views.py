from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import FormularioPost, FormularioRegistro

# Create your views here.

def inicio(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts': posts})


def pages(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'pages.html', {'post':post})


class Subir_post(CreateView):
    model = Post
    form_class = FormularioPost
    template_name = 'subir_post.html'


class Editar_post(UpdateView):
    model = Post
    template_name = 'editar_post.html'
    fields = ['titulo', 'subtitulo', 'cuerpo']


class Eliminar_post(DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = reverse_lazy('inicio')


def usuario_login(request): #Si la llamo login puede haber un conflicto con el módulo
    if request.method =="POST":
        username = request.POST['nombre']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.success(request, 'Error al iniciar. Intente nuevamente.')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def usuario_logout(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('inicio')

def registro(request):
    if request.method =="POST":
        mi_formulario = FormularioRegistro(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
            username = mi_formulario.cleaned_data['username']
            password = mi_formulario.cleaned_data['password1']
            usuario = authenticate(username=username, password=password)
            login(request, usuario)
            messages.success(request, ('¡Usuario registrado correctamente!'))
            return redirect('inicio')
    else:
        mi_formulario = FormularioRegistro()

    return render(request, 'registro.html', {'formulario': mi_formulario})