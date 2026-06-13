from .models import WorkoutStep

from .parsers.running_parser import (
    parse_running_workout
)

from workouts.builders.block_builder import (
    BlockBuilder
)


def generar_steps(workout):

    datos = parse_running_workout(
        workout.descripcion_original
    )

    WorkoutStep.objects.filter(
        workout=workout
    ).delete()

    orden = 1

    for item in datos:

        WorkoutStep.objects.create(
            workout=workout,

            orden=orden,

            tipo=item["tipo"],

            repeticiones=item.get(
                "repeticiones",
                1
            ),

            distancia_metros=item.get(
                "distancia_metros"
            ),

            duracion_segundos=item.get(
                "duracion_segundos"
            ),

            ritmo_objetivo=item.get(
                "ritmo_objetivo",
                ""
            ),

            zona=item.get(
                "zona",
                ""
            ),

            observacion=item.get(
                "observacion",
                ""
            ),           
            
        )

        orden += 1
        
def reparse_workout(workout):

    generar_steps(workout)

    builder = BlockBuilder(
        workout
    )

    builder.build()

    return workout