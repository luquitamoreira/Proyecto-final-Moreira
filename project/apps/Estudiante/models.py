from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.nombre}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.IntegerField()


class Preceptor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()


class Directivo(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
