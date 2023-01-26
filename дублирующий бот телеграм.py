import telebot

bot_token = '5951397436:AAHjhkAAYq2_SeDWykCSffzwo4U3CxZUyBU'
bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(chat_id=message.chat.id, text=message.text)

bot.polling()