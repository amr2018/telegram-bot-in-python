
from telegram.ext import *
import keys

print('start bot')

def start_command(update, context):
    update.message.reply_text('hi i am here help you')

def help_command(update, context):
    update.message.reply_text('hi how i can help you')

def handle_message(update, context):
    msg = str(update.message['text'])
    if 'name' in msg:
        update.message.reply_text('my name is bot')

    if 'age' in msg:
        update.message.reply_text('my age is 18')



updater = Updater(keys.api_key, use_context=True)
db = updater.dispatcher
db.add_handler(CommandHandler('start', start_command))
db.add_handler(CommandHandler('help', help_command))
db.add_handler(MessageHandler(Filters.text, handle_message))


updater.start_polling()
updater.idle()
