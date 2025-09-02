import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import os


load_dotenv()
API_TOKEN = os.getenv('TOKEN')
bot = Bot(token=API_TOKEN)

dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def start(msg: types.Message):
    await msg.reply("✌️ Привіт! Я слухаю твої питання 🙂")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(
        main()
    )
