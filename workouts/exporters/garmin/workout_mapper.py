class GarminWorkoutMapper:

    def map_step(self, step):

        tipo = step["tipo"]

        if tipo == "warmup":

            return {
                "step_type": "warmup",
                "duration":
                    step["duracion_segundos"]
            }

        if tipo == "interval":

            return {

                "step_type": "run",

                "distance":
                    step["distancia_metros"],

                "pace":
                    step["ritmo_objetivo"],
            }

        if tipo == "recovery":

            return {

                "step_type": "recovery",

                "duration":
                    step["duracion_segundos"]
            }

        if tipo == "cooldown":

            return {

                "step_type": "cooldown",

                "duration":
                    step["duracion_segundos"]
            }