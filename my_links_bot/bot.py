import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# ЗАМЕНИ ЭТУ СТРОКУ НА СВОЙ ТОКЕН ОТ @BotFather
BOT_TOKEN = "8566879014:AAEtOVVrKLPMttqdF4Rrno-pT3DU4V7xHS4"

dp = Dispatcher()

# Команда /start показывает меню с кнопками
@dp.message(Command("start"))
async def cmd_start(message: Message):
    # Здесь создаём кнопки. ЗАМЕНИ ССЫЛКИ И ТЕКСТ НА СВОИ.
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📢 Мой Telegram-канал", url="https://t.me/твой_канал")],
            [InlineKeyboardButton(text="▶️ YouTube", url="https://youtube.com/@твой_канал")],
            [InlineKeyboardButton(text="📝 Мой блог", url="https://твой_блог_сайт")],
            [InlineKeyboardButton(text="💻 GitHub", url="https://github.com/твой_профиль")],
        ]
    )
    await message.answer("Привет! Выбирай, куда перейти:", reply_markup=keyboard)

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())