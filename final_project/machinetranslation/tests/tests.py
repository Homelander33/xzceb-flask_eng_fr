import unittest
from translator import french_to_english, english_to_french

class TestTranslator1(unit.testTestcase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Je vous remercie"), "Thank you")

class TestTranslator1(unit.testTestcase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Thank you"), "Je vous remercie")
