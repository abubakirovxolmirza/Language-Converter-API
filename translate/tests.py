from django.test import TestCase
from .converter import convert_text


class TestConverter(TestCase):
    def test_convert_text_cyrillic_to_latin(self):
        context = "Салом Холмирза"

        result = convert_text(context, pattern='latin')
        self.assertEqual(result, "Salom Xolmirza")

    def test_convert_text_latin_to_cyrillic(self):
        context = "Salom Shox"

        result = convert_text(context, pattern='cyrillic')
        self.assertEqual(result, "Салом Щох")

