from django.contrib import admin
from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "activo",
        "fecha_creacion",
    )

    search_fields = (
        "nombre",
    )

    list_filter = (
        "activo",
    )