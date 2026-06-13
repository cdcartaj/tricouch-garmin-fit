class WorkoutBuilder:

    def __init__(self, workout):

        self.workout = workout

    def build(self):

        estructura = []

        for step in self.workout.steps.all():

            estructura.append({

                "id": step.id,

                "tipo": step.tipo,

                "repeticiones": step.repeticiones,

                "distancia_metros":
                    step.distancia_metros,

                "duracion_segundos":
                    step.duracion_segundos,

                "ritmo_objetivo":
                    step.ritmo_objetivo,

                "zona":
                    getattr(
                        step,
                        "zona",
                        ""
                    ),

                "observacion":
                    step.observacion,
            })

        return estructura