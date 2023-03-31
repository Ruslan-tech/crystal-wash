import os
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

bot = Bot(token=os.getenv('API_TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage = storage)
