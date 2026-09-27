import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiohttp import web

BOT_TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📢 Telegram", url="https://t.me/mikha360blog")],
            [InlineKeyboardButton(text="▶️ YouTube", url="https://youtube.com/@Mikha_Anti")],
            [InlineKeyboardButton(text="💬 Мой MAX-канал", url="https://max.ru/join/CV1IFpryHpITGUpYIZUGIfEytnAcKp-vt7DDsN4Flok/")],
            [InlineKeyboardButton(text="💻 GitHub", url="https://github.com//smd1wow-machomen")],
        ]
    )
    await message.answer(
        "👋 Привет! Выбирай, куда перейти:",
        reply_markup=keyboard
    )

async def handle(request):
    return web.Response(text="Bot is alive!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    await start_web_server()
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
