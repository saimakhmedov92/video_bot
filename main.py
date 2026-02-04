import telebot
import yt_dlp

import os

TOKEN = os.getenv("BOT_TOKEN")  # токен загрузим из Railway

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Привет! Отправь мне ссылку на видео, и я его скачаю!")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text

    bot.send_message(message.chat.id, "⏳ Скачиваю видео...")

    try:
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': 'video.mp4'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        video = open("video.mp4", "rb")
        bot.send_video(message.chat.id, video)
        video.close()

        os.remove("video.mp4")

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка: {e}")

bot.infinity_polling()
