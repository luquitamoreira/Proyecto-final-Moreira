from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.

admin.site.register(models.Curso)
admin.site.register(models.Estudiante)
admin.site.register(models.Preceptor)
admin.site.register(models.Directivo)
admin.site.register(models.Profesor)
