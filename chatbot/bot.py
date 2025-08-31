import langdetect
from deep_translator import GoogleTranslator
from chatbot.languages import SUPPORTED_LANGUAGES
from transformers import pipeline

class ChatBotTeacher:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt2", framework="pt")

    def detect_language(self, message):
        return langdetect.detect(message)

    def translate_to_english(self, message, src_lang):
        if src_lang == 'en':
            return message
        return GoogleTranslator(source=src_lang, target='en').translate(message)

    def translate_from_english(self, message, dest_lang):
        if dest_lang == 'en':
            return message
        return GoogleTranslator(source='en', target=dest_lang).translate(message)

    def get_answer(self, message, lang_code):
        english_message = self.translate_to_english(message, lang_code)
        response = self.generator(english_message, max_length=100)
        generated_text = response[0]['generated_text']   # <-- FIXED LINE
        return self.translate_from_english(generated_text, lang_code)
