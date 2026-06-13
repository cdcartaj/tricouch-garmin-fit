class GarminWorkoutBuilder:

    def build(self, estructura):

        resultado = []

        for step in estructura:

            tipo = step["type"]

            if tipo == "interval_set":

                resultado.extend(
                    self._build_interval_set(step)
                )

            else:

                resultado.append(step)

        return resultado

    def _build_interval_set(
        self,
        step
    ):

        resultado = []

        resultado.append({
            "type": "interval",
            "distance": step.get("distance"),
            "pace": step.get("pace"),
            "zone": step.get("zone", "")
        })

        resultado.append({
            "type": "repeat",
            "count": step.get("repeat", 1)
        })

        return resultado