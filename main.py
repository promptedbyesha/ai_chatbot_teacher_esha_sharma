from chatbot.bot import ChatBotTeacher
from ui.cli import run_cli

if __name__ == "__main__":
    bot = ChatBotTeacher()
    run_cli(bot)
