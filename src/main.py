from typing import Any
from dotenv import load_dotenv
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import middlewares
from aiogram.dispatcher.handler import CancelHandler
import re
from middlewares import ReigstrationAccessMiddleware
load_dotenv()

import os
from dbcontext import MongoContext

db = MongoContext()
from commands import dp
from config import bot
# Инициализация бота и диспетчера



# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    
    await message.reply("Привет! Я бот-эхо. Отправь мне что-нибудь, и я повторю это сообщение.")

# @dp.message_handler(lambda message: re.search(r'^/buy_\d+', message.text))
# async def handle_buy_command(message: types.Message):
#     await message.answer(f"Вы написалиasd: {message.text}")
    
# # Обработчик всех текстовых сообщений
# @dp.message_handler(content_types=types.ContentTypes.TEXT)
# async def echo_message(message: types.Message):
#     await message.answer(f"Вы написали: {message.text}")
    
    

    
if __name__ == '__main__':
    db.connect()
    dp.middleware.setup(ReigstrationAccessMiddleware())
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)