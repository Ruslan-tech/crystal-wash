from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

# com_btn_price = KeyboardButton("Цены на услуги")
# com_btn_wash = KeyboardButton("Записаться")

# com_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(com_btn_master, com_btn_client)


"""Create button for choise user position"""
welcome_mrkup = InlineKeyboardMarkup(row_width=2)
welcome_price = InlineKeyboardButton(text='Цены на услуги', callback_data='price_service')
welcome_wash = InlineKeyboardButton(text='Записаться', callback_data='go_wash')
welcome_mrkup.add(welcome_price, welcome_wash)

