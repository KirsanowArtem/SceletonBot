from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

async def show_topic_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        thread_id = update.message.message_thread_id
        chat_id = update.message.chat_id
        print(f"Chat ID: {chat_id}, Thread ID: {thread_id}")
        await update.message.reply_text(f"ID теми: {thread_id}")

app = ApplicationBuilder().token("7924946023:AAFt9uaxUfZqO8Yg_TIqyoExcDfYFwVR4vo").build()
app.add_handler(MessageHandler(filters.ALL, show_topic_id))
app.run_polling()
