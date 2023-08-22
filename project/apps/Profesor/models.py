from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class Profesor(models.Model):
    usuario= models.OneToOneField(User, on_delete=models.CASCADE, related_name="profesor")
    celular = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatares",blank=True,null=True,)


class Venta(models.Model):
    profesor=models.ForeignKey(Profesor,on_delete=models.DO_NOTHING)
    curso=models.ForeignKey("Curso.Curso",on_delete=models.DO_NOTHING)
    precio_total=models.DecimalField(max_digits=10,decimal_places=2,editable=False)
    fecha_venta=models.DateTimeField(default=timezone.now,editable=False)

    class Meta:
        ordering = ("fecha_venta",)

    def clean (self):
        if self.cantidad > self.curso.cantidad:
            raise ValidationError("La cantidad de cursos vendidos han sido superadas")
    
    def save(self,*args,**kargs):
        self.precio_total = self.curso.precio * self.cantidad
        super().save(*args,**kargs)