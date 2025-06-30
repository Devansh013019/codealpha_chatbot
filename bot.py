def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! "
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm a simple chatbot 🤖"
    elif "what can you do" in user_input:
        return "I can chat with you using simple rules!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day "
    elif "how are you" in user_input:
        return "I am fine, thank you! "
    else:
        return "Sorry, I don't understand that. "


print("🤖 ChatBot: Hello! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)
    print("ChatBot:", response)

    if "bye" in user_input.lower():
        break