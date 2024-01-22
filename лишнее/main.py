from telebot import TeleBot
from random import choice

TOKEN = '6138420324:AAEs-WWUKZa0qUPE-TwgJMee9hqWc40DR9w'
bot = TeleBot(TOKEN)

game_choice = ["камень", "ножницы", "бумага"]
user_poinsts = 0
comp_poinsts = 0

@bot.message_handler(func=lambda x: x.text.lower() in game_choice)
def game(message):
    global user_poinsts
    global comp_poinsts
    user_choice = message.text.lower()
    bot_choice = choice(game_choice)
    bot.send_message(message.chat.id, bot_choice)
    if user_choice == "камень" and bot_choice == "ножницы":
        msg = 'победа'
        user_poinsts += 1
    elif user_choice == "бумага" and bot_choice == "камень":
        msg = 'победа'
        user_poinsts += 1
    elif user_choice == "ножницы" and bot_choice == "бумага":
        msg = 'Победа'
        user_poinsts += 1
    elif user_choice == bot_choice:
        msg = 'Ничья'
    else:
        msg = "ты проиграл"
        comp_poinsts += 1
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['points'])
def points(message):
    bot.send_message(message.chat.id, f"бот: {comp_poinsts} игрок: {user_poinsts}")

@bot.message_handler(commands=['reset'])
def reset(message):
    global user_poinsts
    global comp_poinsts
    user_poinsts = 0
    comp_poinsts = 0
    bot.send_message(message.chat.id, "Очки обнулены")

if __name__ == '__main__':
    bot.polling(none_stop=True)
