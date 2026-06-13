class GarminStructureMapper:

    def map(self, estructura):

        resultado = []

        for item in estructura:

            # Warmup

            if item["type"] == "warmup":

                resultado.append({

                    "garmin_type": "warmup",

                    "duration":
                        item["duration"]
                })

            # Steady Run

            elif item["type"] == "steady_run":

                resultado.append({

                    "garmin_type": "run",

                    "distance":
                        item["distance"],

                    "zone":
                        item["zone"],

                    "pace":
                        item["pace"],
                })

            # Recovery

            elif (
                item["type"]
                == "transition_recovery"
            ):

                resultado.append({

                    "garmin_type":
                        "recovery",

                    "duration":
                        item["duration"]
                })

            # Interval Set

            elif (
                item["type"]
                == "interval_set"
            ):

                resultado.append({

                    "garmin_type":
                        "repeat",

                    "repeat":
                        item["repeat"],

                    "distance":
                        item["distance"],

                    "pace":
                        item["pace"],
                })

            # Cooldown

            elif item["type"] == "cooldown":

                resultado.append({

                    "garmin_type":
                        "cooldown",

                    "duration":
                        item["duration"]
                })

        return resultado