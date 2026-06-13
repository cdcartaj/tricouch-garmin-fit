import re


def parse_running_workout(texto):

    resultado = []

    lineas = texto.lower().splitlines()

    for linea in lineas:

        linea = linea.strip()

        if not linea:
            continue

        # -------------------------
        # WARMUP
        # -------------------------

        warmup = re.search(
            r"(calentamiento|warmup)\s*(\d+)\s*min",
            linea
        )

        if warmup:

            resultado.append({
                "tipo": "warmup",
                "duracion_segundos":
                    int(warmup.group(2)) * 60
            })

            continue

        # -------------------------
        # COOLDOWN
        # -------------------------

        cooldown = re.search(
            r"(vuelta a la calma|cooldown)\s*(\d+)\s*min",
            linea
        )

        if cooldown:

            resultado.append({
                "tipo": "cooldown",
                "duracion_segundos":
                    int(cooldown.group(2)) * 60
            })

            continue

        # -------------------------
        # INTERVALOS
        # -------------------------

        intervalo = re.search(
            r"(\d+)x(\d+)m\s*@?\s*(\d+:\d+)",
            linea
        )

        if intervalo:

            resultado.append({
                "tipo": "interval",
                "repeticiones":
                    int(intervalo.group(1)),

                "distancia_metros":
                    int(intervalo.group(2)),

                "ritmo_objetivo":
                    intervalo.group(3)
            })

            continue
        
        # --------------------------------
        # DISTANCIA + ZONA
        # --------------------------------

        distancia_zona = re.search(
            r"(\d+)k\s*(z\d)",
            linea
        )

        if distancia_zona:

            resultado.append({
                "tipo": "interval",

                "distancia_metros":
                    int(distancia_zona.group(1)) * 1000,

                "zona":
                    distancia_zona.group(2).upper()
            })

            continue
        
        # --------------------------------
        # Soportar Ritmo Carrera
        # --------------------------------
        
        ritmo_carrera = re.search(
            r"(\d+)k\s*ritmo",
            linea
        )

        if ritmo_carrera:

            resultado.append({
                "tipo": "interval",

                "distancia_metros":
                    int(ritmo_carrera.group(1)) * 1000,

                "observacion":
                    "ritmo carrera"
            })

            continue

        # --------------------------------
        # Soportar Tiempo
        # --------------------------------
        tiempo = re.search(
            r"^(\d+)\s*min\s*(suave|z1|z2|z3|umbral)?$",
            linea
        )

        if tiempo:

            resultado.append({

                "tipo": "interval",

                "duracion_segundos":
                    int(tiempo.group(1)) * 60,

                "zona":
                    (
                        tiempo.group(2).upper()
                        if tiempo.group(2)
                        else ""
                    )
            })

            continue
        
        # -------------------------
        # RECOVERY
        # -------------------------

        recovery = re.search(
            r"rec\s*(\d+)\s*min",
            linea
        )

        if recovery:

            resultado.append({
                "tipo": "recovery",
                "duracion_segundos":
                    int(recovery.group(1)) * 60
            })

            continue

        # -------------------------
        # RECOVERY En SEGUNDOS
        # -------------------------
        
        recovery_seg = re.search(
            r"rec\s*(\d+)s",
            linea
        )

        if recovery_seg:

            resultado.append({
                "tipo": "recovery",

                "duracion_segundos":
                    int(recovery_seg.group(1))
            })

            continue

    return resultado