import asyncio
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from services import check_prices_and_get_message

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет!\n\n"
        "Я отслеживаю цены на беговые кроссовки Puma (43 размер).\n\n"
        "Доступные команды:\n"
        "/prices — показать 3 самые дешевые модели\n"
        "/check — то же самое (старая команда)"
    )


async def send_prices(update: Update):
    status = await update.message.reply_text(
        "🔎 Проверяю цены... Это занимает 5–10 секунд."
    )

    try:
        text = await asyncio.to_thread(check_prices_and_get_message)

        await status.edit_text(
            text,
            disable_web_page_preview=True,
        )

    except Exception as e:
        await status.edit_text(
            f"❌ Ошибка:\n{e}"
        )


async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_prices(update)


async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_prices(update)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prices", prices))
    app.add_handler(CommandHandler("check", check))

    print("Бот запущен.")

    app.run_polling()


if __name__ == "__main__":
    main()