from aiogram import types, Router
from aiogram.filters import CommandStart, Command
user_privat_router = Router()


@user_privat_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет ,я виртуальный помощник')


@user_privat_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer('Вот меню:')


@user_privat_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('Тут прекрасно кормят:')


@user_privat_router.message(Command('description'))
async def description_cmd(message: types.Message):
    await message.answer('Шумная,веселая пиццерия:')
