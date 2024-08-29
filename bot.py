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
    client_first_name = message.from_user.first_name
    client_last_name = (
        message.from_user.last_name if message.from_user.last_name else "null"
    )
    client_username = message.from_user.username
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Заполнить",
                    web_app=WebAppInfo(
                        url=f"{os.getenv('URL_TO_FRONTEND')}?first_name={client_first_name}&last_name={client_last_name}&username={client_username}"
                    ),
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
