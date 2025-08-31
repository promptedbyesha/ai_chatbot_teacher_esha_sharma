from chatbot.languages import SUPPORTED_LANGUAGES

def run_cli(bot):
    print("Welcome to AI Chatbot Teacher!")
    print(f"Supported languages: {', '.join(SUPPORTED_LANGUAGES.values())}")
    while True:
        user_input = input("Ask your question (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        lang_code = bot.detect_language(user_input)
        answer = bot.get_answer(user_input, lang_code)
        print(answer)
