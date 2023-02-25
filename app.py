from aiogram import executor
from utils.bot_commands import set_default_commands
from loader import dp
import handlers
import utils
import asyncio


async def on_startup(dp):
    await set_default_commands(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
