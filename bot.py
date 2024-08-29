import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from dotenv import load_dotenv


load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")


bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_button(message: Message) -> None:
    """
    Sends a message with button to client.

    :param message: A message that is sent to bot from client.
    :type message: Message
    """
    await message.answer(
        "Привет! Нажми на кнопку ниже, чтобы заполнить дату рождения.",
        reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton("Заполнить", url="https://your-webapp-url.com")
        ),
    )


if __name__ == "__main__":
    dp.run_polling()
