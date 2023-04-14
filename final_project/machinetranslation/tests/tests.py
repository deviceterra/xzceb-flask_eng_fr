import unittest
import translator

class TestTranslation(unittest.TestCase):
    def test_french_to_english_null_input(self):
        self.assertIsNone(translator.frenchToEnglish(None))

    def test_english_to_french_null_input(self):
        self.assertIsNone(translator.englishToFrench(None))

    def test_french_to_english_hello(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')

    def test_english_to_french_hello(self):
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()