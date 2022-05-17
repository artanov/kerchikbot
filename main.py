import asyncio
from aiogram import Bot, Dispatcher, executor, types
from configuration import BOT_TOKEN

import logging

logging.basicConfig(
    format="%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s",
    level=logging.INFO,
)
#######
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
#######


if __name__ == "__main__":
    from handlers import dp

    executor.start_polling(dp)
