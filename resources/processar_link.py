import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

from resources.download_audio import download_audio

async def processar_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = update.message.text
    await update.message.reply_text("🔄 Baixando áudio... Aguarde um momento.")

    arquivo, titulo = download_audio(link)

    if arquivo:
        await update.message.reply_audio(audio=open(arquivo, 'rb'), title=titulo)
        os.remove(arquivo)
    else:
        await update.message.reply_text("❌ Ocorreu um erro ao baixar o áudio.")