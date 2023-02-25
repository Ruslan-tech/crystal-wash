import os

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('API_TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
