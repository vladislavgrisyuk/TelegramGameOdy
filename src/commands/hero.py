from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from repositories.UserRepository import UserRepository
from config import dp # Импортируйте dp из вашего основного модуля
from context.localizedText import LocalizedText
from dbcontext import MongoContext
import textwrap

db = MongoContext()

@dp.message_handler(commands=['hero'])
async def handle_buy_command(message: types.Message):
    # Ваш код обработки команды /buy_...
    user = db.getUserByTelegramId(message.from_user.id)
    
    await message.reply(f'{user.name}')

@dp.message_handler(lambda message: message.text == LocalizedText.hero['ru'])
async def handle_buy_command(message: types.Message):
    # Ваш код обработки команды /buy_...
    ur = UserRepository()
    user = ur.getUserById(message.from_user.id)
    replyStr = textwrap.dedent(f'''
    ☘️{user.name}
    🏅Уровень: 3
    ⚔️Атака: 2 🛡Защита: 1
    ❤️Здоровье: 300/300 /medicine
    🔋Выносливость: 1/5
    💰40
    
    🎒Рюкзак: 0/15 /inv
    📦Склад: 4 /stock
    ⚙️Настройки /settings
    ''')
    await message.reply(replyStr)
    