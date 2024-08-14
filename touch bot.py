import os
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the Telegram bot token from the .env file
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Initialize the bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Function to handle the start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the J. Bunny Game! Tap to make J. Bunny kiss Boozy!")

# Function to handle the tap command
def tap(update: Update, context: CallbackContext):
    # Logic to check if user has tapped 10 times
    # For now, we'll assume the user has tapped 10 times
    update.message.reply_text("J. Bunny kissed Boozy! You've earned 10 J. Bunny tokens!")

# Set up the Updater and Dispatcher
updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add handlers for the start and tap commands
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("tap", tap))

# Start the bot
updater.start_polling()
updater.idle()
