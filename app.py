import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import find_dotenv, load_dotenv

from handler.user_group import user_group_router
from handler.user_privat import user_privat_router
from handler.admin_privat import admin_router
from common.bot_cmds_list import private

load_dotenv(find_dotenv())


ALLOWED_UPDATES = ['message,edit_message']

bot = Bot(token=os.getenv('TOKEN'),default=DefaultBotProperties(parse_mode=ParseMode.HTML))

bot.my_admin_list=[]
dp = Dispatcher()

dp.include_router(user_privat_router)
dp.include_router(user_group_router)
dp.include_router(admin_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
