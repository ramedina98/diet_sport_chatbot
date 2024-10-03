# This class helps me to handle

from bases.diet_knowledge import get_diet_info
from utils.get_plural import get_plural
from utils.process_input import process_input
from utils.synonyms_antonyms import get_synonyms

class SportDietChatbot:
    def __init__(self):
        self.greeting_messages = ["Hola, soy tu asistente de dietas deportivas. ¿Cómo puedo ayudarte?",
                                "¡Hola! ¿Tienes alguna pregunta sobre tu dieta deportiva?"]
        self.farewell_messages = ["Adiós, ¡mantente saludable!", "Hasta luego, ¡sigue con tu entrenamiento!"]

    def get_response(self, user_input):
        """
        Process the user input and return an answer bases in the knoledge base and the rules...
        """
        processed_input = process_input(user_input)
        response = self._handle_intent(processed_input)
        return response

    def _handle_intent(self, processed_input):
        """
        Determines user intent based on the words processed...
        """
        if "adiós" in processed_input or "hasta luego" in processed_input:
            return self._get_farewell_message()

        # check if there is a question about sporte diets...
        response = get_diet_info(processed_input)
        if response:
            return response

        # If there isn`t a match, try with synonyms and plural...
        for word in processed_input:
            synonyms = get_synonyms(word)
            plural_form = get_plural(word)
            if synonyms or plural_form:
                return get_diet_info(synonyms + [plural_form])

        return "Lo siento, no tengo suficiente información sobre ese tema. ¿Puedes ser más específico?"

    def _get_greeting_message(self):
        """
        Returns a greeting at the begening of the conversation...
        """
        import random
        return random.choice(self.greeting_messages)

    def _get_farewell_message(self):
        """
        Returns a goodbye message...
        """
        import random
        return random.choice(self.farewell_messages)