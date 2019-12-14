import os
import requests
from telegram.ext import Updater, CommandHandler

def ola(update, context):
    print('recebi um olá')
    message = f"Tudo bem, {update.message.from_user.first_name}?"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def codigo_de_conduta(update, context):
    print('Recebi um pedido de codigo de conduta')
    url = 'https://raw.githubusercontent.com/pythonrio/codigo-de-conduta/master/README.md'
    try:
        r = requests.get(url)
        text = r.text
        print(text)
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    except Exception as e:
        print(e)

def chama_os_admin(update, context):
    print('ô admin')
    text = '@bianca_rosa @eucld'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


# @pybot_pythonrio_bot
def main():
    token = os.getenv('TELEGRAM_BOT_TOKEN', None)
    if token is None:
        print('token não existe')
    else:
        print('token existe')
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('ola', ola))
    updater.dispatcher.add_handler(CommandHandler('codigo_de_conduta', codigo_de_conduta))
    updater.dispatcher.add_handler(CommandHandler('admin', chama_os_admin))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
