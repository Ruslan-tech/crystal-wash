from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

# com_btn_price = KeyboardButton("Цены на услуги")
# com_btn_wash = KeyboardButton("Записаться")

# com_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(com_btn_master, com_btn_client)


"""Выбор клиентов записи или прайса"""
welcome_mrkup = InlineKeyboardMarkup(row_width=2)
welcome_price = InlineKeyboardButton(text="Цены на услуги", callback_data="car_mrkup")
welcome_wash = InlineKeyboardButton(text="Записаться", callback_data="go_wash")
welcome_qr = InlineKeyboardButton(text="QR-code", callback_data="qr_code")
welcome_mrkup.add(welcome_price, welcome_wash, welcome_qr)

#Категория автомобиля
car_mrkup = InlineKeyboardMarkup(row_width=1)
car_cat_sed = InlineKeyboardButton(text="СЕДАН", callback_data="sedan")
car_cat_cros = InlineKeyboardButton(text="КРОССОВЕР", callback_data="cross")
car_cat_vned = InlineKeyboardButton(text="ВНЕДОРОЖНИК", callback_data="vned")
car_cat_minv = InlineKeyboardButton(text="МИКРОАВТОБУС", callback_data="microbus")
#car_cat = ReplyKeyboardMarkup(resize_keyboard = True).add(car_cat_1, car_cat_2, car_cat_3, car_cat_4)
car_mrkup.add(car_cat_sed, car_cat_cros, car_cat_vned, car_cat_minv)

# Выбор услуги
price_mrkup_sedan = InlineKeyboardMarkup(row_width=1)
price_wash_sedan = InlineKeyboardButton(text="МОЙКА", callback_data="moika_sedan")
price_polish_sedan = InlineKeyboardButton(text="ПОЛИРОВКА", callback_data="polish_sedan")
price_liq_glass_sedan = InlineKeyboardButton(text="ЖИДКОЕ СТЕКЛО", callback_data="liq_glass_sedan")
price_dry_cleaner_sedan = InlineKeyboardButton(text="ХИМЧИСТКА", callback_data="dry_cleaner_sedan")
price_presale_sedan = InlineKeyboardButton(text="ПРЕДПРОДАЖНАЯ ПОДГОТОВКА", callback_data="presale_sedan")
price_prot_cover_sedan = InlineKeyboardButton(text="ЗАЩИТНЫЕ ПОКРЫТИЯ", callback_data="prot_cover_sedan")
price_mrkup_sedan.add(price_wash_sedan, price_polish_sedan, price_liq_glass_sedan, price_dry_cleaner_sedan, price_presale_sedan, price_prot_cover_sedan)


def create_btn_liquid_glass(title: str, price: int, clback: str):
    price_liquid_glass_mrkup = InlineKeyboardMarkup(row_width=1)
    btn_liquid_glass = InlineKeyboardButton(text=f"{title} - от {price} руб.", callback_data=f"{clback}")
    price_liquid_glass_mrkup.add(btn_liquid_glass)
    return price_liquid_glass_mrkup


serv = {"МОЙКА": "moika", "ПОЛИРОВКА": "polish", "ХИМЧИСТКА": "dry_cleaner", "ЗАЩИТНЫЕ ПОКРЫТИЯ": "prot_cover"}


def create_btn_mrkup_services(car_class: str):
    mrkup = InlineKeyboardMarkup(row_width=1)
    for k, v in serv.items():
        btn = InlineKeyboardButton(text=f"{k}", callback_data=f"{v}_{car_class}")
        mrkup.add(btn)
    btn_liq = InlineKeyboardButton(text="ЖИДКОЕ СТЕКЛО", callback_data="liq_glass")
    btn_presale = InlineKeyboardButton(text="ПРЕДПРОДАЖНАЯ ПОДГОТОВКА", callback_data="presale")
    mrkup.add(btn_liq, btn_presale)
    return mrkup


def create_btn(lst):
    mrkup = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)
    i = 0
    for el in lst:
        btn = InlineKeyboardButton(text=f"{el}", callback_data=f"{i + 1}")
        i += 1
        mrkup.add(btn)
    btn_back = InlineKeyboardButton(text="Вернуться к выбору типа авто -->", callback_data="car_mrkup")
    mrkup.add(btn_back)
    return mrkup