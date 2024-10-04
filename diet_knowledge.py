# diet_knowledge.py
from bases.knwoledge_base import diet_info

def get_diet_info(processed_input):
    """
    Returns relevant information about diets bases in the user input...
    """
    # Search if any key word is in the kwoledge base...
    for word in processed_input:
        if word in diet_info:
            return diet_info[word]

    return None