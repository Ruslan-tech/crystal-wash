from aiogram import Bot, Dispatcher, types
#from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode
import logging
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from aiogram.types import ContentType, Message
from loader import dp, bot
from aiogram.types import Message
import cv2
import requests
import numpy
from qrcode.image.pure import PyPNGImage
from PIL import Image
import io
import os


from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

ADMIN = 5130842598 #Твой личный ID узнать можно здесь https://t.me/getmyid_arel_bot

print("Admin")

async def is_admin(user_id):
    return user_id == ADMIN

class dialog(StatesGroup):
    waiting_for_news = State()
    waiting_for_confirmation = State()
    qr = State()

@dp.message_handler(commands=['admin'])
async def admin_command(message: Message):
    if await is_admin(message.from_user.id):
        await message.reply("Привет! Вы находитесь а административной панели!")
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = KeyboardButton('Сканировать QR-code')
        button2 = KeyboardButton('Рассылка')
        keyboard.add(button1, button2)
        await message.answer('Выберите действие:', reply_markup=keyboard)
    else:
        await bot.send_message(chat_id=message.chat.id,
                               text="Вы не авторизованы для доступа к этой панели.")


@dp.message_handler(commands=['cancel'], state='*')
async def cancel_command(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Отменено.')



@dp.message_handler(lambda message: message.text == 'Рассылка')
async def spam(message: Message):
  await dialog.waiting_for_news.set()
  await message.answer('Напиши текст рассылки')

@dp.message_handler(content_types=types.ContentType.PHOTO, state=dialog.waiting_for_news)
async def start_spam(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['news'] = message.photo[-1].file_id

        keyboard_D = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_D.add(types.KeyboardButton(text="Да"))
        keyboard_D.add(types.KeyboardButton(text="Нет"))

        await dialog.next()
        await message.reply("Вы уверены что хотите отправить это сообщение?", reply_markup=keyboard_D)


@dp.message_handler(Text(equals="Да"), state=dialog.waiting_for_confirmation)
async def send_news(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        news = data['news']

        # Отправляем новость всем пользователям
        # users = get_users_from_database()
        # for user in users:
        #     try:
        #         await bot.send_message(user['id'], news)
        #     except Exception as e:
        #         logging.exception("Error sending news to user %s: %s", user['id'], e)

        await message.answer("Новость успешно отправлена.")
        await state.finish()

@dp.message_handler(Text(equals="Нет"), state=dialog.waiting_for_confirmation)
async def cancel_sending(message: types.Message, state: FSMContext):
    await message.answer("Отменено.")
    await state.finish()

@dp.message_handler(lambda message: message.text == 'Сканировать QR-code')
async def spam(message: Message):
  await dialog.qr.set()
  await message.answer('Отправь фотографию QR-code')

@dp.message_handler(state=dialog.qr, content_types=ContentType.PHOTO)
async def start_spam(message: Message, state: FSMContext):
    if message.text == 'Назад':
        #это не работет но пока оставлю
        print("exit qr")
        #выход организован в else
        await state.finish()
    else:
        photo_file_id = message.photo[-1].file_id
        #print(photo_file_id)
        file_photo = await bot.get_file(photo_file_id)
        file_path = file_photo.file_path
        url_info = f"https://api.telegram.org/file/bot{os.getenv('API_TOKEN')}/"
        img = requests.get(url_info+file_path)
        img_b = Image.open(io.BytesIO(img.content))
        #из байт кода в массив
        open_cv_image = numpy.array(img_b)
        #декодируем qr-code
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(open_cv_image)
        if data == "":
            message_adm = "Ошибка QR-code. Попробуйте еще раз."
        if data.find("cry: ") == 0:
            message_adm = "QR-code. Успешно просканирован."
            #####работа с БД######
            to_BD_user = data[5:]
            print(to_BD_user)
            ######################
        else:
            message_adm = "Неверный QR-code."
                
        await message.reply(text = message_adm)
        await state.finish()       

