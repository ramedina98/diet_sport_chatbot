# This is the main file of the diet sport chatbot...
from classes.SportDietChatBot import SportDietChatbot
from utils.noAccents import noAccents
# import nltk
# nltk.download('wordnet')

# Iniciar el chatbot
if __name__ == "__main__":
    chatbot = SportDietChatbot()
    print(chatbot._get_greeting_message())

    while True:
        user_input = input("Tú: ")
        cleaned_input = noAccents(user_input)
        if "adios" in cleaned_input.lower():
            print("Chatbot:", chatbot._get_farewell_message())
            break
        response = chatbot.get_response(cleaned_input.lower())
        print("Chatbot:", response)