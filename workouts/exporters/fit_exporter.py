from fit_tool.fit_file_builder import (
FitFileBuilder
)

from fit_tool.profile.messages.workout_message import (
WorkoutMessage
)

from fit_tool.profile.messages.workout_step_message import (
WorkoutStepMessage
)

from fit_tool.profile.messages.file_id_message import (
FileIdMessage
)

from fit_tool.profile.messages.file_creator_message import (
FileCreatorMessage
)

class FitExporter:

    def export(
        self,
        workout_name,
        mensajes,
        filename
    ):

        builder = FitFileBuilder()

        file_id = FileIdMessage()

        file_id.type = 5
        file_id.manufacturer = 1
        file_id.product = 65534

        builder.add(
            file_id
        )

        file_creator = FileCreatorMessage()

        file_creator.software_version = 2610
        file_creator.hardware_version = 0

        builder.add(
            file_creator
        )

        workout_msg = WorkoutMessage()

        workout_msg.workout_name = workout_name

        workout_msg.sport = 1

        workout_msg.capabilities = 32

        workout_msg.num_valid_steps = 6

        builder.add(
            workout_msg
        )

        index = 0

        for mensaje in mensajes:

            if mensaje["message"] == "repeat":

                step = WorkoutStepMessage()

                step.message_index = index

                #
                # Garmin FIT SDK:
                # repeat_until_steps_cmplt
                #
                step.duration_type = 6

                #
                # volver al paso del intervalo
                #
                step.duration_value = 3

                #
                # open
                #
                step.target_type = 2

                #
                # cantidad de repeticiones
                #
                step.target_value = mensaje["count"]

                print("\nREPEAT EXPORT")

                print(
                    "duration_type =",
                    step.duration_type
                )

                print(
                    "duration_value =",
                    step.duration_value
                )

                print(
                    "target_type =",
                    step.target_type
                )

                print(
                    "target_value =",
                    step.target_value
                )

                builder.add(step)

                index += 1

                continue

            if mensaje["message"] != "workout_step":
                continue

            step = WorkoutStepMessage()

            step.message_index = index

            # Valores por defecto
            step.target_type = 0
            step.target_value = 0

            if "target_pace" in mensaje:

                step.custom_target_value_low = 3448
                step.custom_target_value_high = 4082
                
            if "target_zone" in mensaje:

                zona = mensaje["target_zone"]

                if zona == "Z2":

                    step.target_type = 0

                    step.target_value = 0

                    #
                    # Z2 = 5:30 - 6:00
                    #
                    step.custom_target_value_low = 2778

                    step.custom_target_value_high = 3030

            if "duration_type" in mensaje:

                print(
                    "RAW duration_type =",
                    repr(
                        mensaje.get(
                            "duration_type"
                        )
                    )
                )

                if mensaje["duration_type"] == "time":

                    step.duration_type = 0

                    step.duration_value = (
                        mensaje["duration_value"]
                    )

                elif mensaje["duration_type"] == "distance":

                    step.duration_type = 1

                    step.duration_value = (
                        mensaje["duration_value"] / 10
                    )

            if "intensity" in mensaje:

                intensidad = mensaje["intensity"]

                if intensidad == "active":

                    step.intensity = 0
                    step.target_type = 0
                    step.target_value = 0

                elif intensidad == "warmup":

                    step.intensity = 2

                    step.target_type = 0
                    step.target_value = 0

                    step.duration_type = 1

                    #
                    # 15 min -> aprox 2.5 km
                    #
                    step.duration_value = 250

                    step.custom_target_value_low = 2778
                    step.custom_target_value_high = 3030

                elif intensidad == "cooldown":

                    step.intensity = 3

                    step.target_type = 0
                    step.target_value = 0

                    step.duration_type = 1

                    #
                    # 10 min -> aprox 1 km
                    #
                    step.duration_value = 100

                    step.custom_target_value_low = 2778
                    step.custom_target_value_high = 3030

                elif intensidad == "recovery":

                    step.intensity = 4
                    step.target_type = 2
                    step.target_value = 0
                    
                    step.duration_value = 120000

            index += 1

            print("STEP EXPORT")
            print("duration_type =", step.duration_type)
            print("duration_value =", step.duration_value)
            print("intensity =", step.intensity)
            
            print(
                "target_type =",
                step.target_type
            )

            print(
                "target_value =",
                step.target_value
            )

            print(
                "low =",
                step.custom_target_value_low
            )

            print(
                "high =",
                step.custom_target_value_high
            )

            builder.add(step)

        fit_file = builder.build()

        fit_file.to_file(
            filename
        )

        return filename
