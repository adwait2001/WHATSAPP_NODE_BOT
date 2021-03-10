 
import sys
import process as pc

print(pc.sms_reply(sys.argv[1]))    ### second argument phone number tak
# print(sys.argv[1])



    
'''
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
TOKEN = '1419554707:AAHxlCK_AFnO0ZHXziImCSvG222hUs8k40k'
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
 
def start(update,context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello! welcome to cricket turf \n lets book your slot and save time and save 5% too')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def response(update, context):
    """Echo the user message."""
    try: 
      cust= update.message.chat.first_name + update.message.chat.last_name
    except:
      cust = update.message.chat.first_name  
    print(cust)
    
    pm = "You said: "+update.message.text#sms_reply(update.message.text,cust) 
    bot = telegram.Bot(token=TOKEN)       
    #print(bot.updates)
    if pm=="xae12":
        bot.sendPhoto(chat_id=update.message.chat.id, photo=open(r'mytable.png', 'rb'))
    else:
        bot.send_message(chat_id = update.message.chat.id,text=pm)
    


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, response))

    # log all errors
    
    #dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

def start():
    if __name__ == '__main__':
        main()

start()'''

 
