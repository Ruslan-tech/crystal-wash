from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

com_btn_master = KeyboardButton("Мастер")
com_btn_client = KeyboardButton("Клиент")

com_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(com_btn_master, com_btn_client)


"""Create button for choise user position"""
welcome_mrkup = InlineKeyboardMarkup(row_width=2)
welcome_master = InlineKeyboardButton(text='Мастер', callback_data='Мастер')
welcome_client = InlineKeyboardButton(text='Клиент', callback_data='Клиент')
welcome_mrkup.add(welcome_master, welcome_client)


"""Create button for choise master position"""
position_mrkup = InlineKeyboardMarkup(row_width=2)
position_cosmetolog = InlineKeyboardButton(text='Косметолог', callback_data='Косметолог')
position_vizajist = InlineKeyboardButton(text='Визажист', callback_data='Визажист')
position_massage = InlineKeyboardButton(text='Массажист', callback_data='Массаж')
position_manik_ped = InlineKeyboardButton(text='Мастер маникюра/педикюра', callback_data='Маникюр/Педикюр')
position_mrkup.add(position_cosmetolog, position_vizajist, position_massage, position_manik_ped)