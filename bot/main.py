import asyncio
import logging
import os

from aiogram.filters import Command
from dotenv import load_dotenv
load_dotenv()

from aiogram import Bot, Dispatcher, types
from loguru import logger

# Удаляем стандартный обработчик
logger.remove()
# Настраиваем логирование в файл с ограничением количества файлов
logger.add(
    "loggs.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
    rotation="5 MB",  # Ротация файла каждые 10 MB
    retention="10 days",  # Хранить только 5 последних логов
    compression="zip",  # Сжимать старые логи в архив
    backtrace=True,     # Сохранение трассировки ошибок
    diagnose=True       # Подробный вывод
)

TOKEN = os.getenv('iamgroot')

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command(commands="start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я работаю в Docker 🐳")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logger.info('включение бота')
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.exception('выключение бота')