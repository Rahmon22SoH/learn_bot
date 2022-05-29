import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # Импортируем нужные компоненты

logging.basicConfig(
    level=logging.INFO,
    filename = 'bot.log',
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

# С любым прокси выдаёт ошибку PROXY = IndentationError: unexpected indent


# Функция, которая соединяется с платформой Telegram
def greed_user(update, context):
    print("Вызван /start")
    update.message.reply_text('Привет пользователь! Ты вызвал команду /start')
    print(update)

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context = True) 
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greed_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('start bot')
    mybot.start_polling() # запросы за обновлениями
    mybot.idle # бесконечный цикл бота

# Экранируем вызов main() 
# 'Вызов функций прямо на верхнем уровне считается плохим стилем и в дальнейшем вызовет проблемы'
if __name__ == "__main__":
    main()