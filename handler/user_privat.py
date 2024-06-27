from aiogram import F, types, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChaTypeFilter
from kbds.replay import get_keyboard

user_privat_router = Router()
user_privat_router.message.filter(ChaTypeFilter(['private']))


@user_privat_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        'Привет ,я виртуальный помощник',
        reply_markup=get_keyboard(
            "Меню",
            "О магазине",
            "Варианты оплаты",
            "Варианты доставки",
            placeholder="Что вас интересует?",
            sizes=(2, 2),
        ),
    )


@user_privat_router.message(or_f(Command('menu'), (F.text.lower() == 'меню')))
async def menu_cmd(message: types.Message):
    await message.answer('Вот меню:')


@user_privat_router.message((F.text.lower().contains('инфа')) | (F.text.lower() == 'о магазине'))
@user_privat_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('Тут прекрасно кормят:')


@user_privat_router.message((F.text.lower().contains('плата')) | (F.text.lower() == 'варианты оплаты'))
@user_privat_router.message(Command('payment'))
async def payment_cmd(message: types.Message):

    text = as_marked_section(
        Bold("Варианты оплаты:"),
        "Картой в боте",
        "При получении карта/кеш",
        "В заведении",
        marker='✔️'
    )
    await message.answer(text.as_html())


@user_privat_router.message((F.text.lower().contains('достав')) | (F.text.lower() == 'варианты доставки'))
@user_privat_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold("Варианты доставки/заказа"),
            "Курьер",
            "Самовынос (сейчас забегу заберу)",
            "Покушаю у Вас (сейчас прибегу)",
            marker='✅'
        ),
        as_marked_section(
            Bold("Нельзя:"),
            "Почта",
            "Голуби",
            marker='❌'
        ),
        sep='\n------------------------------------------------------\n'
    )
    await message.answer(text.as_html())


@user_privat_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"номер получен")
    await message.answer(str(message.contact))


@user_privat_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"Локация получена")
    await message.answer(str(message.location))
