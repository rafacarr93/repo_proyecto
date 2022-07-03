from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Post

class FormularioPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'cuerpo','imagen','autor')

    widgets = {
        'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
        'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        'imagen': forms.ImageField(),
        'autor': forms.Textarea(attrs={'class': 'form-control'}),
    }

class FormularioRegistro(UserCreationForm):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField(widget=forms.EmailInput())
    web = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'nombre', 'email', 'web', 'password1', 'password2')

class FormularioEditarUsuario(UserChangeForm):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField(widget=forms.EmailInput())
    web = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'nombre', 'email', 'web', 'password')