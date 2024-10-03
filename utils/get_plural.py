def get_plural(word):
    """
    Returns the plural form of a word
    """
    if word.endswith('a'):
        return word[:-1] + 'as'
    elif word.endswith('o'):
        return word[:-1] + 'os'
    return word + 's'