from django.contrib import admin

# Register your models here.
from . import models
admin.site.site_header="Administracion de Cursos"
admin.site.site_title = "Cursos"

# admin.site.register(models.ProductoCategoria)


@admin.register(models.CursoCategoria)
class CursoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_filter = ("nombre",)
    search_fields = ("nombre", "descripcion")
    ordering = ("nombre",)

@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display=(
    "categoria" ,
    "nombre",
    "cantidad_de_horas",
    "modalidad",
    "precio" ,
    "descripcion",
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering =(
        "categoria",
        "nombre",
    )
    list_filter=("categoria",)
    search_fields=("nombre",)