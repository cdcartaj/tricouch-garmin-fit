from django.test import TestCase

from workouts.parsers.running_parser import (
    parse_running_workout
)


class RunningParserTest(TestCase):

    def test_interval_training(self):

        texto = """
        Calentamiento 15 min

        8k Z2

        rec 2 min

        6x1000m @4:35

        Vuelta a la calma 10 min
        """

        resultado = parse_running_workout(
            texto
        )

        self.assertEqual(
            resultado[0]["tipo"],
            "warmup"
        )

        self.assertEqual(
            resultado[1]["tipo"],
            "interval"
        )

        self.assertEqual(
            resultado[2]["tipo"],
            "recovery"
        )

        self.assertEqual(
            resultado[3]["tipo"],
            "interval"
        )

        self.assertEqual(
            resultado[4]["tipo"],
            "cooldown"
        )
