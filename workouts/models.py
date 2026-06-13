from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):

    SPORT_CHOICES = (
        ("run", "Running"),
        ("bike", "Cycling"),
        ("swim", "Swimming"),
        ("brick", "Brick"),
    )

    nombre = models.CharField(
        max_length=200
    )

    deporte = models.CharField(
        max_length=20,
        choices=SPORT_CHOICES
    )

    descripcion_original = models.TextField()

    creador = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    activo = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.nombre
    
class WorkoutStep(models.Model):

    STEP_TYPES = (
        ("warmup", "Warm Up"),
        ("interval", "Interval"),
        ("recovery", "Recovery"),
        ("cooldown", "Cool Down"),
        ("rest", "Rest"),
    )

    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name="steps"
    )

    orden = models.PositiveIntegerField()

    tipo = models.CharField(
        max_length=20,
        choices=STEP_TYPES
    )

    repeticiones = models.PositiveIntegerField(
        default=1
    )

    distancia_metros = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    duracion_segundos = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    ritmo_objetivo = models.CharField(
        max_length=20,
        blank=True
    )

    observacion = models.TextField(
        blank=True
    )
    
    zona = models.CharField(
        max_length=20,
        blank=True
    )

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return f"{self.workout} - {self.tipo}"
    
class WorkoutExport(models.Model):

    FORMATS = (
        ("tcx", "TCX"),
        ("fit", "FIT"),
        ("zwo", "ZWO"),
    )

    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE
    )

    formato = models.CharField(
        max_length=10,
        choices=FORMATS
    )

    fecha_generacion = models.DateTimeField(
        auto_now_add=True
    )

    archivo = models.FileField(
        upload_to="exports/"
    )
    
class WorkoutBlock(models.Model):

    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name="blocks"
    )

    nombre = models.CharField(
        max_length=100
    )

    orden = models.IntegerField()

    repeticiones = models.IntegerField(
        default=1
    )

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.nombre
    
