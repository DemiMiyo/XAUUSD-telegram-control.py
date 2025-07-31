import telebot
import json
import os

BOT_TOKEN = "8437888512:AAEWEB95_T0Cd_wNVok8EDFCP0zgSjrkZKo"
bot = telebot.TeleBot(BOT_TOKEN)

STATE_FILE = "bot_state.json"

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

def load_state():
    if not os.path.exists(STATE_FILE):
        save_state({"running": False})
    with open(STATE_FILE, 'r') as f:
        return json.load(f)

@bot.message_handler(commands=['start'])
def start_handler(message):
    state = load_state()
    state['running'] = True
    save_state(state)
    bot.reply_to(message, "✅ Trading bot started.")

@bot.message_handler(commands=['stop'])
def stop_handler(message):
    state = load_state()
    state['running'] = False
    save_state(state)
    bot.reply_to(message, "🛑 Trading bot stopped.")

@bot.message_handler(commands=['status'])
def status_handler(message):
    state = load_state()
    running = state.get("running", False)
    bot.reply_to(message, f"📊 Bot status: {'Running' if running else 'Stopped'}")

bot.polling()
