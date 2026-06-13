class GarminFitDebugExporter:

    def export(self, estructura):

        resultado = []

        for step in estructura:

            tipo = step["type"]

            if tipo == "warmup":

                resultado.append({
                    "message": "workout_step",
                    "intensity": "warmup",
                    **step
                })

            elif tipo == "steady_run":

                resultado.append({
                    "message": "workout_step",
                    "intensity": "active",
                    **step
                })

            elif tipo == "transition_recovery":

                resultado.append({
                    "message": "workout_step",
                    "intensity": "recovery",
                    **step
                })

            elif tipo == "interval":

                resultado.append({
                    "message": "workout_step",
                    "intensity": "active",
                    **step
                })

            elif tipo == "repeat":

                resultado.append({
                    "message": "repeat",
                    **step
                })

            elif tipo == "cooldown":

                resultado.append({
                    "message": "workout_step",
                    "intensity": "cooldown",
                    **step
                })

        return resultado