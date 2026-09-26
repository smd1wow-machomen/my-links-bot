import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiohttp import web

BOT_TOKEN = "ТВОЙ_ТОКЕН"  # Лучше брать из переменной окружения, но для теста можно так

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📢 Telegram", url="https://t.me/твой_канал")],
            [InlineKeyboardButton(text="▶️ YouTube", url="https://youtube.com/@твой_канал")],
        ]
    )
    await message.answer("Выбирай:", reply_markup=keyboard)

# --- Мини-сервер для Render, чтобы он не усыплял бота ---
async def handle(request):
    return web.Response(text="Bot is alive!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 10000)  # Render сам подставит порт
    await site.start()

async def main():
    # Запускаем веб-сервер и бота одновременно
    await start_web_server()
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
