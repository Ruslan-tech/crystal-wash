from aiogram import types
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from keyboards.client_kb import welcome_mrkup
from utils.dbmanage.dbcontrol import client_exists, add_client_to_db

from loader import dp, bot


@dp.message_handler(CommandStart)
async def start_welcome(message: types.message):
    if not client_exists(message.from_user.id):
        add_client_to_db(message.from_user.id, message.from_user.username)
    
    await bot.send_message(message.from_user.id, text=f"Hello! {message.from_user.username}", 
                           reply_markup=welcome_mrkup)