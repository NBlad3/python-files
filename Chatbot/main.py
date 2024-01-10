import telebot
from datetime import date
import schedule

chat_id = ""
bot_token = "6917775042:AAEAckkT3ArHGHxQRI6GSurkrdXXOdZtbC4"

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands = ["start"])
def start_msg(msg):
    global chat_id
    chat_id = msg.chat.id
    bot.reply_to(msg, "System starting...")

@bot.message_handler(commands= ["help"])
def help(msg):
    bot.reply_to(msg, "These are all commands:\n/start - The bot will welcome you\n/<Workday> - The bot will tell you what lessons you have (example: /Mon or /Thu)")

tkb = {
    "Mon": ["Am nhac", "Duc", "Sinh", "Toan"],
    "Tue": ["Phap", "Am nhac", "Duc", "Sinh hoc"],
    "Wed": ["Anh", "Vat ly", "Toan"],
    "Thu": ["Phap", "Anh", "Toan", "Lich su", "Dia ly"],
    "Fri": ["Anh", "Phap", "The duc"]
}

@bot.message_handler(commands= ["Mon", "Tue", "Wed", "Thu", "Fri"])
def subject(msg):
    text_msg = ""
    for x in range(len(tkb[msg.text[1:]])):
        text_msg += tkb[msg.text[1:]][x]
        text_msg += "\n"
    bot.reply_to(msg, text_msg)

def send_daily_schedule():
    global chat_id
    current_day = date.today().strftime("%a")
    if current_day in tkb:
        bot.send_message(chat_id, f"\n- {', '.join(tkb[current_day])}")

bot.polling()
