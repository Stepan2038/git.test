from telebot import TeleBot
import requests

TOKEN = '6667775185:AAHefO-xFmdP0w3f2ov8Al4RyOEucl5Mqfc'
bot = TeleBot(TOKEN)

def random_duck():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.message_handler(commands=['duck'])
def duck(message):
    url = random_duck()
    bot.send_message(message.chat.id, url)


def random_fox():
    url = 'https://randomfox.ca/floof'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.message_handler(commands=['fox'])
def fox(message):
    url = random_fox()
    bot.send_message(message.chat.id, url)

if __name__ == '__main__':
    bot.polling(none_stop=True)