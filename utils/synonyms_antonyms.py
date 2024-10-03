# synonyms_antonyms.py
from nltk.corpus import wordnet

def get_synonyms(word):
    """
    Retuns a list of synonyms of a word using wordnet...
    """
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

def get_antonyms(word):
    """
    Returns a list of antonyms of a word using wordnet...
    """
    antonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    return antonyms