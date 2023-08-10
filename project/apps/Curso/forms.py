from django import forms
from . import models

class CursoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.CursoCategoria
        fields = "__all__"

class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = "__all__"