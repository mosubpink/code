import telebot
from pytube import YouTube
import os
from decouple import config
from telebot.types import BotCommand 
from telebot import types

key = config('Tokein')
bot = telebot.TeleBot(key)

command = [
	BotCommand("start", "start bot"),
	BotCommand("download", "download video")
]

PATH = "./down/"
if os.path.exists(PATH):
	pass
else:
    os.mkdir("down")
bot.set_my_commands(command)
@bot.message_handler(commands=["start"])
def send_welcome(message):
	bot.send_message(message.chat.id, text="hi")+str(message.chat.first_name)("I`M your youtube downloader")

@bot.message_handler(commands=["download"])
def respone(message):
	url_msg = bot.send_message(message.chat.id, text="paste youtube link to download")
	bot.register_next_step_handler(url_msg, Downloading)
def Downloading(message):
    link = message.text
    bot.send_message(message.chat.id, "download starting...")
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4')
    ytdl = yt.streams.get_highest_resolution().download(PATH)
    with open(ytdl, 'rb') as dled :
        bot.send_video(message.chat.id, video=dled)
print("running.....")
bot.polling()
