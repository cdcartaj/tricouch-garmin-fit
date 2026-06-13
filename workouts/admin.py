from django.contrib import admin

from .models import (
    Workout,
    WorkoutStep,
    WorkoutBlock,
    WorkoutExport,
)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "deporte",
        "creador",
        "fecha_creacion",
    )

    list_filter = (
        "deporte",
        "activo",
    )

    search_fields = (
        "nombre",
    )
    
@admin.register(WorkoutStep)
class WorkoutStepAdmin(admin.ModelAdmin):

    list_display = (
        "workout",
        "orden",
        "tipo",
        "repeticiones",
        "distancia_metros",
        "duracion_segundos",
        "ritmo_objetivo",
    )
    
@admin.register(WorkoutBlock)
class WorkoutBlockAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "workout",
        "orden",
        "repeticiones",
    )

@admin.register(WorkoutExport)
class WorkoutExportAdmin(admin.ModelAdmin):

    list_display = (
        "workout",
        "formato",
        "fecha_generacion",
    )

    list_filter = (
        "formato",
    )
