import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message when command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        f"Hi {user.mention_html()}! I'm your first portfolio bot.\n"
        f"Available commands:\n"
        f"/start - show this message\n"
        f"/help - get help\n"
        f"/advice - get programming advice\n"
        f"/quote - get random quote"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message when command /help is issued."""
    await update.message.reply_text("I'm a portfolio bot. Just send me one of the commands!")


async def give_advice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send random programming advice."""
    advice_list = [
        "Make regular Git commits with clear messages.",
        "Write clean code with meaningful comments.",
        "Don't be afraid to ask questions.",
        "Learn something new every day.",
        "Build portfolio projects, not just study theory."
    ]
    advice = random.choice(advice_list)
    await update.message.reply_text(f"💡 Programming advice: {advice}")


async def give_quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send random inspirational quote."""
    quotes = [
        "«The best way to predict the future is to invent it.» — Alan Kay",
        "«Code is poetry.» — WordPress",
        "«Premature optimization is the root of all evil.» — Donald Knuth",
        "«If it works, don't touch it.» — Developer wisdom"
    ]
    quote = random.choice(quotes)
    await update.message.reply_text(quote)


def main():
    """Start the bot."""
    # GET YOUR TOKEN from @BotFather
    TOKEN = "8227826822:AAE9nmsnShYNyS8WBZcBOFhSbuQ14QC_H34"

    # Create Application
    application = Application.builder().token(TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("advice", give_advice))
    application.add_handler(CommandHandler("quote", give_quote))

    # Start bot
    print("Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()