import telebot
import yt_dlp

TOKEN = "8248428620:AAFm8_fwmd-h4nu5MB-HZdvmpprIOSxltwE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Привет! Отправь ссылку на видео, и я скачаю его для тебя.")

@bot.message_handler()
def download_video(message):
    url = message.text

    bot.send_message(message.chat.id, "⏳ Скачиваю, подожди немного...")

    try:
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': 'video.mp4'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        video = open('video.mp4', 'rb')
        bot.send_video(message.chat.id, video)
        video.close()

    except Exception as e:
        bot.send_message(message.chat.id, "❌ Ошибка! Проверь ссылку.")

bot.polling(none_stop=True)
