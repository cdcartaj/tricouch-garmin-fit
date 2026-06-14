from django.urls import path

from . import views

urlpatterns = [

    path(
        "",
        views.workout_list,
        name="workout_list"
    ),

    path(
        "nuevo/",
        views.workout_create,
        name="workout_create"
    ),
    
    path(
        "<int:pk>/",
        views.workout_detail,
        name="workout_detail"
    ),
    
    path(
        "<int:pk>/export/tcx/",
        views.export_tcx,
        name="export_tcx"
    ),
    
    path(
        "<int:pk>/export/fit/",
        views.export_fit,
        name="export_fit"
    ),
    
    path(
        "<int:pk>/reparse/",
        views.workout_reparse,
        name="workout_reparse"
    ),
    
    
   
]