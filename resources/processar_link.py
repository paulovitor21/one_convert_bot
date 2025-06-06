import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import re
from telegram import InputFile
from resources.download_audio import download_audio


def is_youtube_link(link):
    # Aceita links youtube.com ou youtu.be
    return bool(re.match(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/', link))

def clear_name(nome):
    return re.sub(r'[\\/*?:"<>|]', "", nome)

async def processar_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = update.message.text
    if not is_youtube_link(link):
        await update.message.reply_text("❌ Por favor, envie um link válido do YouTube.")
        return
    await update.message.reply_text("🔄 Baixando áudio... Aguarde um momento.")

    arquivo, titulo = download_audio(link)


    if arquivo:
        try:
            nome = clear_name(titulo)
            with open(arquivo, 'rb') as audio:
                await update.message.reply_audio(audio=InputFile(audio, filename=f"{nome}.mp3"), title=titulo)
        except Exception as e:
            await update.message.reply_text(f"Erro ao enviar áudio: {e}")
        finally:
            os.remove(arquivo)
    else:
        await update.message.reply_text("❌ Ocorreu um erro ao baixar o áudio.")