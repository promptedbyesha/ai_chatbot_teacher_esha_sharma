from chatbot.bot import ChatBotTeacher

def test_language_detection():
    bot = ChatBotTeacher()
    assert bot.detect_language("Hello") == "en"
    assert bot.detect_language("नमस्ते") == "hi"
    assert bot.detect_language("హలో") == "te"

def test_get_answer():
    bot = ChatBotTeacher()
    answer = bot.get_answer("What is photosynthesis?", "en")
    assert answer is not None
