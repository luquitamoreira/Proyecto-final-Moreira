from django.db import models

# Create your models here.
class CursoCategoria(models.Model):
    """Categorías de curso """
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        """Representa una instancia de la clase como una cadena de texto"""
        return self.nombre

    class Meta:
        verbose_name = "categoría de cursos"
        verbose_name_plural = "categorías de cursos"


class Curso(models.Model):

    categoria = models.ForeignKey(CursoCategoria,on_delete=models.SET_NULL,blank=True,null=True)
    nombre= models.CharField(max_length=100)
    cantidad_de_horas=models.CharField(max_length=100)
    modalidad= models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    descripcion = models.CharField(max_length=250,null=True,blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.precio}"