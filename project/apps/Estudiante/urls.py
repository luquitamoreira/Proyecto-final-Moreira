from django.urls import path
from .views import home , crear_estudiante

app_name="Estudiante"

urlpatterns = [
    path("", home,name='home'),
    path("crear/", crear_estudiante , name= "crear"),
]
