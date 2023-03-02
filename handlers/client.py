from aiogram import types, Bot, executor, Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from keyboards.client_kb import welcome_mrkup, price_mrkup_sedan, car_mrkup, create_btn, create_btn_mrkup_services
from utils.dbmanage.dbcontrol import client_exists, add_client_to_db, delete_client, get_price_wash
import json
from loader import dp, bot


@dp.message_handler(commands=['start'])
async def start_welcome(message: types.message):
    # add_client_to_db(message.from_user.id, message.from_user.username)
        
    await bot.send_message(message.from_user.id, text=f"Hello! {message.from_user.username}", 
                            reply_markup=welcome_mrkup)
    # if not client_exists(message.from_user.id):
    #     add_client_to_db(message.from_user.id, message.from_user.username)
        
    #     await bot.send_message(message.from_user.id, text=f"Hello! {message.from_user.username}", 
    #                         reply_markup=welcome_mrkup)
    
    # else:
    #     await bot.send_message(message.from_user.id, text="Если нужна помощь, нажми1 /help")
    



@dp.callback_query_handler(text="go_wash")
async def go_wash(callback: types.CallbackQuery):
    await callback.message.answer(text="Для записи на автомоечный комплекс позвоните по телефону +7(965)766-66-55")


@dp.callback_query_handler(text="car_mrkup")
async def go_cat(callback: types.CallbackQuery):
    await callback.message.answer(text="Рассчитайте стоимость Вашего заказа за 1 минуту!", reply_markup=car_mrkup)

cars_types = {"sedan": "седан", "cross": "кроссовер", "vned": "внедорожник", "van": "минивэн"}

cars_service_types = {"moika_sedan": {2: "седан"}, "moika_cross": {3: "кроссовер"}, "moika_vned": {4: "внедорожник"}, "moika_van": {5: "минивэн"}}

@dp.callback_query_handler()
async def get_services_wash_car(callback: types.CallbackQuery):    
    if callback.data in cars_types.keys():
        await callback.message.answer(text=f"Выберите услугу для {cars_types.get(callback.data)}а", 
                                      reply_markup=create_btn_mrkup_services(callback.data))
    elif callback.data in cars_service_types.keys():
        await callback.message.answer(text=f"Цены на услугу МОЙКА {[v for v in cars_service_types.get(callback.data).values()][0]}а", 
                                      reply_markup=create_btn(get_price_wash([k for k in cars_service_types.get(callback.data).keys()][0])))

   

@dp.message_handler(commands=['quit'])
async def delete_client(message: types.message):
    delete_client(message.from_user.id)
    await bot.send_message(message.from_user.id, text="Жаль, что вы нас покидаете. Мы ждем Вас снова.")


@dp.message_handler(commands=['location'])
async def info(message: types.message):
    await bot.send_message(message.from_user.id, text="Коломяжский пр., д. 19 (территория АЗС «ЛИНОС»)\nВыборгская наб., д. 57, лит. А (территория АЗС «ЛИНОС»).")
    
    
@dp.message_handler(commands=['hello'])
async def start_command(message: types.Message):
    await message.answer('<em>Hello,word!</em>', parse_mode="HTML")