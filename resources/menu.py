from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Callback do menu principal
async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() # confirma o clique
    opcao = query.data

    if opcao == "mp3":
        await query.edit_message_text("Envie o link do YouTube para baixar como MP3.")
    else:
        await query.edit_message_text("Opção inválida. Por favor, tente novamente.")
    