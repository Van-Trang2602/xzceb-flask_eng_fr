'''import the library'''
from deep_translator import MyMemoryTranslator

def english_to_french(englishtext):
    """
    Translates English text to French using MyMemoryTranslator.

    Parameters:
    englishtext (str): The English text to be translated.

    Returns:
    str: The translated French text.
    """
    translated = MyMemoryTranslator(source='en', target='french').translate(englishtext)
    return translated

def french_to_english(frenchtext):
    """
    Translates French text to English using MyMemoryTranslator.

    Parameters:
    frenchtext (str): The French text to be translated.

    Returns:
    str: The translated English text.
    """
    translated = MyMemoryTranslator(source='fr', target='en').translate(frenchtext)
    return translated
