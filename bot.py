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
URL_TO_FRONTEND = os.getenv("URL_TO_FRONTEND")


bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_message_with_button_to_client(message: Message) -> None:
    """
    Sends a message with button to client that opens Telegram Web App.

    :param message: A message that is sent to bot from client.
    :type message: Message
    """
    arguments_of_start_command = message.text.split(" ")
    if len(arguments_of_start_command) > 1:
        keyboard_markup = get_button_to_client_info_page(arguments_of_start_command[1])
    else:
        keyboard_markup = get_button_to_birthday_selecting_page(message)
    await message.answer(
        "Привет! Нажми на кнопку ниже, чтобы заполнить дату рождения.",
        reply_markup=keyboard_markup,
    )


def get_button_to_birthday_selecting_page(message: Message) -> InlineKeyboardMarkup:
    """
    Returns a button that opens Telegram Web App and makes redirect to birthday selecting page.

    :param message: A message that is sent to bot from client.
    :type message: Message

    :return: A button that opens Telegram Web App and makes redirect to birthday selecting page.
    :rtype: InlineKeyboardMarkup
    """
    client_first_name = message.from_user.first_name
    client_last_name = (
        message.from_user.last_name if message.from_user.last_name else "null"
    )
    client_username = message.from_user.username
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Заполнить",
                    web_app=WebAppInfo(
                        url=f"{URL_TO_FRONTEND}?first_name={client_first_name}&last_name={client_last_name}&username={client_username}"
                    ),
                )
            ]
        ]
    )


def get_button_to_client_info_page(
    argument_of_start_command: str,
) -> InlineKeyboardMarkup:
    """
    Returns a button that opens Telegram Web App and makes redirect to client info page.

    :param argument_of_start_command: An argument of start command.
    :type argument_of_start_command: str

    :return: A button that opens Telegram Web App and makes redirect to client info page.
    :rtype: InlineKeyboardMarkup
    """
    web_app_url = f"{URL_TO_FRONTEND}/" + "/".join(argument_of_start_command.split("_"))
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть информацию о клиенте",
                    web_app=WebAppInfo(url=web_app_url),
                )
            ]
        ]
    )


if __name__ == "__main__":
    dp.run_polling(bot)
