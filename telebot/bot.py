import telebot
import configure

client = telebot.TeleBot(configure.config['token'])

@client.message_handler(content_types=["text"])
def get_text(message):
    if message.text.lower() == 'привет':
        client.send_message(message.chat.id, 'Привет, неизвестный пользователь!')



client.polling(none_stop = True, intrval = 0)