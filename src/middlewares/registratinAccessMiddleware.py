from aiogram import middlewares
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler


class ReigstrationAccessMiddleware(middlewares.BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data):
        # await update.message.reply('ТЫ ПИДОРАС')
        # raise CancelHandler()
        pass