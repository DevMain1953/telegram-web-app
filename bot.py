import os
from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)
from aiogram.filters import Command
from dotenv import load_dotenv


load_dotenv()
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")


bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_message_with_button_to_client(message: Message) -> None:
    """
    Sends a message with button to client that opens Telegram Web App.

    :param message: A message that is sent to bot from client.
    :type message: Message
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Заполнить", web_app=WebAppInfo(url="https://to-do")
                )
            ]
        ]
    )
    await message.answer(
        "Привет! Нажми на кнопку ниже, чтобы заполнить дату рождения.",
        reply_markup=keyboard,
    )


if __name__ == "__main__":
    dp.run_polling(bot)
