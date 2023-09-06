from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import dp # Импортируйте dp из вашего основного модуля
from dbcontext import MongoContext
from repositories import UserRepository
ur = UserRepository()
kb = ReplyKeyboardMarkup(resize_keyboard=True)
str1 = '⚔️Меч'
str2 = '🗡Клинок'
str3 = '🛡Щит'
listStr = [str1,str2,str3]
bt1 = KeyboardButton(str1)
bt2 = KeyboardButton(str2)
bt3 = KeyboardButton(str3)

kb.row(bt1, bt2)
kb.row(bt3)

db = MongoContext()
#getWeapons
# Обработчик для команд вида /buy_...
@dp.message_handler(commands=['shop'])
async def handle_buy_command(message: types.Message):
    # Ваш код обработки команды /buy_...
    await message.reply("Что хочешь взять?", reply_markup=kb)
    
@dp.message_handler(lambda message: message.text in listStr)
async def handle_buy_command(message: types.Message):
    replyText = 'Вот наши мечи!\n'
    for weapon in db.getWeapons():
        replyText += f'⚔️{weapon.name}\n'
        replyText += f'💰{weapon.price}\n'
        replyText += f'Купить: /buy_{weapon.weaponId}'
        replyText += f'\n'
        replyText += f'\n'
    await message.reply(text=replyText)
    
@dp.message_handler(lambda message: '/buy_' in message.text)
async def handle_buy_command(message: types.Message):
    user = ur.getUserByTelegramId(message.from_user.id)
    weapon = db.getWeaponModel(weaponId=message.text.split('_')[1])
    if(not weapon):
         await message.reply(text='Такого оружия нету')
    if(user):
        if(user.money < weapon.price):
            await message.reply(text='У вас недостаточно денег(')
        else:
            ur.AddItem(message.from_user.id, weapon.id)
            await message.reply(text=f'{weapon.name} добавлен в ваш инвентарь!')
            
    #await message.reply(text=db.getWeapons(weaponId=message.text.split('_')[1])[0].name)
        