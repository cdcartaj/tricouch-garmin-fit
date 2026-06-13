from django.shortcuts import render

from .models import Athlete


def athlete_list(request):

    athletes = Athlete.objects.select_related(
        "user",
        "team"
    )

    return render(
        request,
        "athletes/athlete_list.html",
        {
            "athletes": athletes
        }
    )