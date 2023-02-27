from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

# com_btn_price = KeyboardButton("Цены на услуги")
# com_btn_wash = KeyboardButton("Записаться")

# com_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(com_btn_master, com_btn_client)


"""Выбор клиентов записи или прайса"""
welcome_mrkup = InlineKeyboardMarkup(row_width=2)
welcome_price = InlineKeyboardButton(text='Цены на услуги', callback_data='car_mrkup')
welcome_wash = InlineKeyboardButton(text='Записаться', callback_data='go_wash')
welcome_mrkup.add(welcome_price, welcome_wash)

#Категория автомобиля
car_mrkup = InlineKeyboardMarkup(row_width=1)
car_cat_1 = InlineKeyboardButton(text='Седан', callback_date='1')
car_cat_2 = InlineKeyboardButton(text='Кроссовер', callback_date='2')
car_cat_3 = InlineKeyboardButton(text='Внедорожник', callback_date='3')
car_cat_4 = InlineKeyboardButton(text='Минивен', callback_date='4')
#car_cat = ReplyKeyboardMarkup(resize_keyboard = True).add(car_cat_1, car_cat_2, car_cat_3, car_cat_4)
car_mrkup.add(car_cat_1, car_cat_2, car_cat_3, car_cat_4)







price_mrkup = InlineKeyboardMarkup(row_width=1)
price_wash = InlineKeyboardButton(text="МОЙКА2", callback_data="moika")
price_polish = InlineKeyboardButton(text="ПОЛИРОВКА", callback_data="polish")
price_liq_glass = InlineKeyboardButton(text="ЖИДКОЕ СТЕКЛО", callback_data="liq_glass")
price_dry_cleaner = InlineKeyboardButton(text="ХИМЧИСТКА", callback_data="dry_cleaner")
price_presale = InlineKeyboardButton(text="ПРЕДПРОДАЖНАЯ ПОДГОТОВКА", callback_data="presale")
price_prot_cover = InlineKeyboardButton(text="ЗАЩИТНЫЕ ПОКРЫТИЯ", callback_data="prot_cover")
price_mrkup.add(price_wash, price_polish, price_liq_glass, price_dry_cleaner, price_presale, price_prot_cover)