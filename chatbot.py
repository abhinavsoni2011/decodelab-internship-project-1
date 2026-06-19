responses = {
    "hello": "Hello! How can I help you?",
    "hii" : "Hii! Nice to meet you.",
    "hola amigo" :"Hola, ¿cómo estás?",
    "नमस्ते" : "नमस्ते, आपसे मिलकर अच्छा लगा।",
    "Nǐ hǎo" :"嘿，嗨，你好嗎？",
    "hi": "Hi! Nice to meet you.",
    "how are you": "I am fine. Thank you!",
    "name": "My name is AI Bot.",
    "help": "I can answer simple questions.",
    "bye": "Goodbye! Have a nice day.",

    # English
    "hello": "Hello! How can I help you?",
    "hi": "Hello! How can I help you?",
    "hey": "Hello! How can I help you?",

    # Hindi
    "namaste": "Namaste! Aap kaise hain?",
    "namaskar": "Namaste! Aap kaise hain?",

    # Urdu
    "assalamualaikum": "Wa Alaikum Assalam!",

    # Spanish
    "hola": "¡Hola! ¿Cómo estás?",

    # French
    "bonjour": "Bonjour! Comment allez-vous?",

    # German
    "hallo": "Hallo! Wie geht es Ihnen?",

    # Italian
    "ciao": "Ciao! Come stai?",

    # Portuguese
    "ola": "Olá! Como vai você?",

    # Russian
    "privet": "Привет! Как дела?",

    # Japanese
    "konnichiwa": "こんにちは! お元気ですか?",

    # Chinese
    "ni hao": "你好! 你好吗?",

    # Korean
    "annyeong": "안녕하세요!",

    # Arabic
    "marhaba": "مرحبا! كيف حالك؟",

    # Punjabi
    "sat sri akal": "Sat Sri Akal!",

    # Gujarati
    "kem cho": "Majama?",

    # Bengali
    "nomoskar": "Nomoskar!",

    # Other intents
    "how are you": "I am fine. Thank you!",
    "name": "My name is RuleBot.",
    "help": "I can answer predefined questions.",
    "bye": "Goodbye! Have a great day."
}

print("=== Rule-Based AI Chatbot ===")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")
    user_input = user_input.lower().strip()

    if user_input == "exit":
        print("AI Bot: Goodbye!")
        break
    else:
        reply = responses.get(
            user_input,
            "Sorry, I don't understand that command."
        )
        print("AI Bot:", reply)
