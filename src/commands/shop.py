from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import CommandStart

from config import dp # Импортируйте dp из вашего основного модуля

# Обработчик для команд вида /buy_...
@dp.message_handler(commands=['buy'])
async def handle_buy_command(message: types.Message):
    # Ваш код обработки команды /buy_...
    await message.reply("Вы выбрали команду покупки.")