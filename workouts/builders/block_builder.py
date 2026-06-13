from workouts.models import (
    WorkoutBlock,
    WorkoutStep,
)


class BlockBuilder:

    def __init__(self, workout):

        self.workout = workout

    def build(self):

        WorkoutBlock.objects.filter(
            workout=self.workout
        ).delete()

        orden = 1

        warmup = self.workout.steps.filter(
            tipo="warmup"
        )

        if warmup.exists():

            WorkoutBlock.objects.create(
                workout=self.workout,
                nombre="Warmup",
                orden=orden,
            )

            orden += 1

        interval = self.workout.steps.filter(
            tipo="interval"
        )

        recovery = self.workout.steps.filter(
            tipo="recovery"
        )

        if interval.exists():

            repeticiones = (
                interval.first().repeticiones
            )

            WorkoutBlock.objects.create(
                workout=self.workout,
                nombre="Main Set",
                orden=orden,
                repeticiones=repeticiones,
            )

            orden += 1

        cooldown = self.workout.steps.filter(
            tipo="cooldown"
        )

        if cooldown.exists():

            WorkoutBlock.objects.create(
                workout=self.workout,
                nombre="Cooldown",
                orden=orden,
            )