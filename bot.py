from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Нажми на кнопку ниже, чтобы заполнить дату рождения.",
        reply_markup=types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("Заполнить", url="https://your-webapp-url.com")
        ),
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
