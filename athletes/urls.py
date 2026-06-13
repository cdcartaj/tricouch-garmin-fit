from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.athlete_list,
        name="athlete_list"
    ),
]