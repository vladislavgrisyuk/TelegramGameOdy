from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from context.localizedText import LocalizedText

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

bt1 = KeyboardButton(LocalizedText.hero['ru'])
bt2 = KeyboardButton('H..e.asd.ll.o1 🤖')
bt3 = KeyboardButton('H..e..llasd.o2 🤖')
bt4 = KeyboardButton('H..e..llasd.o3 🤖')

keyboard.row(bt1, bt2)
keyboard.row(bt3, bt4)