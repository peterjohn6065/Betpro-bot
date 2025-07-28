from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes
from keep_alive import start_webserver
import threading
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")  # Example: BetProNetwork
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID"))   # Example: 1227342059

application = Application.builder().token(BOT_TOKEN).build()

# Start keep_alive webserver in background
threading.Thread(target=start_webserver).start()

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to BetPro Bot! Type /help to see available commands.")

# Command: /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Available commands:\n/start – Welcome Message\n/help – List Commands")

# Only admin can access this
async def admin_only(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_USER_ID:
        await update.message.reply_text("🔐 Welcome Admin!")
    else:
        await update.message.reply_text("🚫 You are not authorized to use this command.")

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("admin", admin_only))

print("✅ Bot is running...")
application.run_polling()
