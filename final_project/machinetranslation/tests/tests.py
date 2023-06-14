import unittest
import translator as tr 

class TranslationTests(unittest.TestCase):
    def test_english_to_french_hello(self):
        result = tr.english_to_french("hello")
        self.assertEqual(result, "bonjour")

    def test_french_to_english_bonjour(self):
        result = tr.french_to_english("Bonjour")
        self.assertEqual(result, "Hello")

    def test_french_to_english_hello(self):
        result = tr.french_to_english("Hello")
        self.assertNotEqual(result, "Bonjour")

    def test_english_to_french_bonjour(self):
        result = tr.english_to_french("Bonjour")
        self.assertNotEqual(result, "Hello")

if __name__ == '__main__':
    unittest.main()