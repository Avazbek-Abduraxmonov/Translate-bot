import requests
import telebot

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(msg):
    cid = msg.chat.id
    bot.send_message(cid , 'Assalomu Aleykum botimga xush kelibsiz! Bu bot sizga Ingliz tilidan Uzbek tiliga ogirib beradi')


@bot.message_handler(func=lambda message: True)
def add(msg):
    url = "https://text-translator2.p.rapidapi.com/translate"

    payload = {
        "source_language": "en",
        "target_language": "uz",
        "text": msg.text
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "34fe6d2e50msh7e10501cd13c417p19e723jsnc12607a15468",
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    data = response.json().get('data').get('translatedText')
    bot.send_message(msg.chat.id, data)
print(bot.get_me())
bot.polling()
