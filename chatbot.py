# This is the main file of the diet sport chatbot...
from classes.SportDietChatBot import SportDietChatbot

# Iniciar el chatbot
if __name__ == "__main__":
    chatbot = SportDietChatbot()
    print(chatbot._get_greeting_message())

    while True:
        user_input = input("Tú: ")
        if "adiós" in user_input.lower():
            print("Chatbot:", chatbot._get_farewell_message())
            break
        response = chatbot.get_response(user_input.lower())
        print("Chatbot:", response)