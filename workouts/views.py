from django.shortcuts import render
from django.shortcuts import redirect

from .models import Workout
from .forms import WorkoutForm
from .services import generar_steps, reparse_workout
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .exporters.tcx_exporter import (
    export_workout_to_tcx
)

from workouts.builders.block_builder import (
    BlockBuilder
)



def workout_list(request):

    workouts = Workout.objects.all()

    return render(
        request,
        "workouts/workout_list.html",
        {
            "workouts": workouts
        }
    )

def workout_detail(request, pk):

    workout = get_object_or_404(
        Workout,
        pk=pk
    )

    return render(
        request,
        "workouts/workout_detail.html",
        {
            "workout": workout
        }
    )

def workout_create(request):

    if request.method == "POST":

        form = WorkoutForm(request.POST)

        if form.is_valid():

            workout = form.save(commit=False)

            if request.user.is_authenticated:
                workout.creador = request.user

            workout.save()
            
            generar_steps(workout)
            
            builder = BlockBuilder(workout)

            builder.build()

            return redirect("workout_list")

    else:

        form = WorkoutForm()

    return render(
        request,
        "workouts/workout_form.html",
        {
            "form": form
        }
    )

def workout_reparse(request, pk):

    workout = get_object_or_404(
        Workout,
        pk=pk
    )

    reparse_workout(workout)

    return redirect(
        "workout_detail",
        pk=workout.id
    )
    
def export_tcx(request, pk):

    workout = get_object_or_404(
        Workout,
        pk=pk
    )

    tcx = export_workout_to_tcx(
        workout
    )

    response = HttpResponse(
        tcx,
        content_type="application/xml"
    )

    response[
        "Content-Disposition"
    ] = (
        f'attachment; '
        f'filename="{workout.nombre}.tcx"'
    )

    return response