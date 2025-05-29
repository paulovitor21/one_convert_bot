import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import yt_dlp
import uuid

# Caminho do ffmpeg.exe
#FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"  # <<< MUITO IMPORTANTE: coloque o caminho correto aqui

def download_audio(url, output_dir="downloads"):
    try:
        os.makedirs(output_dir, exist_ok=True)
        temp_id = str(uuid.uuid4())
        output_template = os.path.join(output_dir, f'{temp_id}.%(ext)s')

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_template,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            #'ffmpeg_location': FFMPEG_PATH,  # <<< Aqui está passando o caminho do ffmpeg,
            'noplaylist': True,
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'audio')


        mp3_path = os.path.join(output_dir, f"{temp_id}.mp3")
        if os.path.isfile(mp3_path):
            print(f"Arquivo gerado: {mp3_path}")
            return mp3_path, title
        else:
            print(f"Arquivo mp3 nao encontrado: {mp3_path}")
            return None, None

    except Exception as e:
        print(f'Erro ao baixar audio: {e}')
        return None, None
