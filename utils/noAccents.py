# This function helps me to clean a string get in away all the accents...
import unicodedata

def noAccents(text):
    return ''.join(
        (c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    )