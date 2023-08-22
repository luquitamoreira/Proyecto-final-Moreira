from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Profesor)



@admin.register(models.Venta)
class ProfesorAdmin(admin.ModelAdmin):
    list_display= (
        "profesor",
        "curso",
        "precio_total",
        "fecha_venta",

    )

    list_display_links=("curso",)
    search_fields =("curso.nombre","profesor")
    list_filter= ("profesor",)
    date_hierarchy = "fecha_venta"