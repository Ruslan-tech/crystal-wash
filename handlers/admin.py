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

ADMIN = 5130842598

print("Admin")

#фиксируем прилет qr-code
@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):   
    #Сохраняем картинку на серверах телеги и запихиваем ее в переменную ввиде байт кода
    photo_file_id = message.photo[-1].file_id
    print(photo_file_id)
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
    print(data)
    print(bbox)
    print(straight_qrcode)
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

