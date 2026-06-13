from django.db import models

class Team(models.Model):

    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    descripcion = models.TextField(
        blank=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    activo = models.BooleanField(
        default=True
    )
    
    
    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre