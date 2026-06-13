from xml.etree import ElementTree as ET
from xml.etree.ElementTree import (
    Element,
    SubElement,
    tostring,
)


def export_workout_to_tcx(workout):

    root = ET.Element(
        "TrainingCenterDatabase"
    )

    workouts = ET.SubElement(
        root,
        "Workouts"
    )

    workout_xml = ET.SubElement(
        workouts,
        "Workout"
    )

    name = ET.SubElement(
        workout_xml,
        "Name"
    )

    name.text = workout.nombre

    for step in workout.steps.all():

        step_xml = ET.SubElement(
            workout_xml,
            "Step"
        )

        tipo = ET.SubElement(
            step_xml,
            "Type"
        )

        tipo.text = step.tipo

        if step.distancia_metros:

            distancia = ET.SubElement(
                step_xml,
                "DistanceMeters"
            )

            distancia.text = str(
                step.distancia_metros
            )

        if step.duracion_segundos:

            duracion = ET.SubElement(
                step_xml,
                "DurationSeconds"
            )

            duracion.text = str(
                step.duracion_segundos
            )

        if step.ritmo_objetivo:

            ritmo = ET.SubElement(
                step_xml,
                "TargetPace"
            )

            ritmo.text = (
                step.ritmo_objetivo
            )

    return ET.tostring(
        root,
        encoding="utf-8",
        xml_declaration=True
    )
    

class TCXExporter:

    def export(self, workout_name, estructura):

        root = Element(
            "TrainingCenterDatabase"
        )

        workouts = SubElement(
            root,
            "Workouts"
        )

        workout = SubElement(
            workouts,
            "Workout",
            Sport="Running"
        )

        workout.set(
            "Name",
            workout_name
        )

        for step in estructura:

            self._add_step(
                workout,
                step
            )

        return tostring(
            root,
            encoding="unicode"
        )

    def _add_step(
        self,
        workout,
        step
    ):

        item = SubElement(
            workout,
            "Step"
        )

        item.set(
            "Type",
            step["type"]
        )

        for key, value in step.items():
            if key == "type":
                continue

            if value is None:
                continue

            if value == "":
                continue

            field = SubElement(
                item,
                key
            )

            field.text = str(value)
            
    def export_to_file(
        self,
        workout_name,
        estructura,
        filename
    ):

        xml = self.export(
            workout_name,
            estructura
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(xml)

        return filename
            
