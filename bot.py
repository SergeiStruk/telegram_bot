import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start command handler
async def start(update: Update, context) -> None:
    await update.message.reply_text("Hello World!")

# Message handler for non-command messages
async def echo(update: Update, context) -> None:
    await update.message.reply_text("Hello World!")

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        logger.error("TELEGRAM_TOKEN environment variable not found")
        return

    # Create the application
    application = ApplicationBuilder().token(token).build()

    # Add command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
