from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.handler import CancelHandler
from repositories.UserRepository import UserRepository
from config import dp # Импортируйте dp из вашего основного модуля
from keyboards.mainMenuKeyBoard import keyboard

@dp.message_handler(commands=['main'])
async def handle_buy_command(message: types.Message):
    # Ваш код обработки команды /buy_...
    
    await message.reply(text='/main',reply_markup=keyboard)

