from django.contrib import admin

from .models import Athlete


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "team",
        "ftp",
        "fc_max",
        "activo",
    )

    list_filter = (
        "team",
        "activo",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
    )
    
