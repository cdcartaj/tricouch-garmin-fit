from django.db import models
from django.contrib.auth.models import User

from teams.models import Team


class Athlete(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    fecha_nacimiento = models.DateField(
        null=True,
        blank=True
    )

    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    ftp = models.IntegerField(
        null=True,
        blank=True,
        help_text="FTP ciclismo"
    )

    fc_max = models.IntegerField(
        null=True,
        blank=True
    )

    ritmo_10k = models.CharField(
        max_length=20,
        blank=True
    )

    ritmo_70_3 = models.CharField(
        max_length=20,
        blank=True
    )

    activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username