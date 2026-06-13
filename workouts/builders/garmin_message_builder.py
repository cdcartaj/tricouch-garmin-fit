class GarminMessageBuilder:

    def build(
        self,
        workout_name,
        estructura
    ):

        mensajes = []

        mensajes.append({
            "message": "workout",
            "sport": "running",
            "name": workout_name,
            "num_steps": len(estructura)
        })

        for step in estructura:

            mensajes.append(
                self._map_step(step)
            )

        return mensajes

    def _map_step(
        self,
        step
    ):

        tipo = step["type"]

        if tipo == "warmup":

            return {
                "message": "workout_step",
                "duration_type": "time",
                "duration_value": step["duration"],
                "intensity": "warmup"
            }

        elif tipo == "steady_run":

            return {
                "message": "workout_step",
                "duration_type": "distance",
                "duration_value": step["distance"],
                "target_zone": step.get(
                    "zone",
                    ""
                ),
                "intensity": "active"
            }

        elif tipo == "transition_recovery":

            return {
                "message": "workout_step",
                "duration_type": "time",
                "duration_value": step["duration"],
                "intensity": "recovery"
            }

        elif tipo == "interval":

            return {
                "message": "workout_step",
                "duration_type": "distance",
                "duration_value": step["distance"],
                "target_pace": step.get(
                    "pace",
                    ""
                ),
                "intensity": "active"
            }

        elif tipo == "repeat":

            return {
                "message": "repeat",
                "count": step["count"]
            }

        elif tipo == "cooldown":

            return {
                "message": "workout_step",
                "duration_type": "time",
                "duration_value": step["duration"],
                "intensity": "cooldown"
            }

        return {
            "message": "unknown"
        }