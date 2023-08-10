from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
#Importaciones para el login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
from . import models,forms
#PAGINA PRINCIPAL

@login_required
def index (request):
    return render(request,'Curso/index.html')

#LIST

#def cursocategoria_list(request):
#    categorias = models.CursoCategoria.objects.all()
#    context = {"object_list":categorias}
#    return render(request,"Curso/cursocategoria_list.html",context)

class CursoCategoriaList(ListView):
    model = models.CursoCategoria

class CursoCategoriaCreate(CreateView):
    model = models.CursoCategoria
    form_class = forms.CursoCategoriaForm
    success_url = reverse_lazy("Curso:cursocategoria_list")


#CREATE 

#def cursocategoria_create(request: HttpRequest )-> HttpResponse:
#    if request.method == "POST":
#        form = forms.CursoCategoriaForm(request.POST)
#        if form.is_valid():
#            form.save()
##            return redirect("Curso:home")
#    else:
#        form = forms.CursoCategoriaForm()
#    return render(request,"Curso/cursocategoria_form.html",{"form":form})

#DETAIL
class CursoCategoriaDetail(DetailView):
    model = models.CursoCategoria
#UPDATE
class CursoCategoriaUpdate(UpdateView):
    model = models.CursoCategoria
    form_class = forms.CursoCategoriaForm
    success_url = reverse_lazy("Curso:cursocategoria_list")
#DELETE
class CursoCategoriaDelete(DeleteView):
    model = models.CursoCategoria
    success_url = reverse_lazy("Curso:cursocategoria_list")

#--------CURSO
#LIST
class CursoList(ListView):
    model = models.Curso
#CREATE 
class CursoCreate(CreateView):
    model=models.Curso
    form_class = forms.CursoForm
    success_url = reverse_lazy("Curso:curso_list")
#DETAIL
class CursoDetail(DetailView):
    model = models.Curso


#UPDATE
class CursoUpdate(UpdateView):
    model = models.Curso
    form_class=forms.CursoForm
    success_url = reverse_lazy("Curso:curso_list")



#DELETE
class CursoDelete(DeleteView):
    model = models.Curso
    success_url = reverse_lazy("Curso:curso_list")

