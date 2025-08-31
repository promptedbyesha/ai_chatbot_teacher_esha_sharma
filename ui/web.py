import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from chatbot.bot import ChatBotTeacher
from chatbot.languages import SUPPORTED_LANGUAGES

st.title("AI Chatbot Teacher")
bot = ChatBotTeacher()

user_message = st.text_input("Ask your question:")

if st.button("Submit"):
    if user_message:
        lang_code = bot.detect_language(user_message)
        answer = bot.get_answer(user_message, lang_code)
        st.write(f"({SUPPORTED_LANGUAGES[lang_code]}) {answer}")
