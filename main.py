import asyncio 
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import ChatJoinRequest
from config_reader import config


logging.basicConfig(level=logging.INFO)

async def request(chat_join: ChatJoinRequest, bot):
    msg = f'Добро пожаловать в канал'
    await bot.send_message(chat_id=chat_join.from_user.id, text=msg)
    await chat_join.approve()


async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    tgk = config.tgk.get_secret_value()
    dp = Dispatcher()
    dp.chat_join_request.register(request, F.chat.id == int(tgk))
    await dp.start_polling(bot)


if __name__=='__main__':
    asyncio.run(main())
