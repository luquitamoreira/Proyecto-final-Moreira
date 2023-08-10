from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpRequest,HttpResponse
from . import forms
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def home(request):
    return render(request,'Home/index.html')

#Login
def login_request(request:HttpRequest) ->HttpResponse:
    if request.method == 'POST':
       form = forms.CustomAuthenticationForm(request,request.POST)
       if form.is_valid():
           usuario= form.cleaned_data.get("username")
           contraseña = form.cleaned_data.get("password")
           user = authenticate(username=usuario,password=contraseña)
           if user is not None:
               login(request,user)
               return render(request,"Home/index.html",{"mensaje":"Inicio sesion correctamente"})
    else:
        form = forms.CustomAuthenticationForm
    return render(request,"Home/login.html",{"form":form})

#Registro
@staff_member_required
def register(request:HttpRequest) ->HttpResponse:
    if request.method == 'POST':
       form = forms.CustomUserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return render(request,"Home/index.html",{"mensaje":"Usuario creado"})

    else:
        form = forms.CustomUserCreationForm
    return render(request,"Home/register.html",{"form":form})