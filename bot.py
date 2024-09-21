from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler

AWAITING_RESPONSE = 1


async def start(update: Update, context) -> int:
        menu_message = """
    Список команд:
    /start - список команд
    /greeting - привітання
    /pic - фотка
    /sum <number1> <number2> - сума двох чисел.
    """
        await update.message.reply_text(menu_message)


async def handle_next_message(update: Update, context) -> int:
    user_message = update.message.text
    await update.message.reply_text('Супер!')
    return ConversationHandler.END


async def cancel(update: Update, context) -> int:
    await update.message.reply_text("Conversation canceled.")
    return ConversationHandler.END


async def pic(update: Update, context) -> None:
    image_url = 'https://i.imghippo.com/files/UuqwT1724107267.jpg'
    await update.message.reply_photo(photo=image_url)


async def sum(update: Update, context) -> None:
    args = context.args

    if len(args) == 2:
        number1 = int(args[0])
        number2 = int(args[1])
        await update.message.reply_text(f'Ізі, це буде {number1 + number2}')
    else:
        await update.message.reply_text('Чібупеліч, введи 2 числа пліз')

async def greeting(update: Update, context) -> None:
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f'Здаров, {user_name}, як справи?')
    return AWAITING_RESPONSE


if __name__ == '__main__':
    application = ApplicationBuilder().token(
        '7202524020:AAFaUCROkhLa67Pvv4IcTOiN_061OHHwVSE').build()

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('greeting', greeting)],
        states={
            AWAITING_RESPONSE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND,
                               handle_next_message)
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(conversation_handler)

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('pic', pic))
    application.add_handler(CommandHandler('sum', sum))
    application.add_handler(CommandHandler('greeting', greeting))

    application.run_polling()
