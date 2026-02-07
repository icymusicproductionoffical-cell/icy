import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎶 Welcome to IYC Music Production Bot!\n\n"
        "Commands:\n"
        "/help - Show commands\n"
        "/about - About us"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start bot\n"
        "/help - Commands\n"
        "/about - About IYC Music Production"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎧 IYC Music Production\n"
        "We create music for you at a reasonable price.\n"
        "DM for collaborations 🎵"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("about", about))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

