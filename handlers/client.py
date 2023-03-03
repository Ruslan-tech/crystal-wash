from aiogram import types, Bot, executor, Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from keyboards.client_kb import welcome_mrkup, price_mrkup_sedan, car_mrkup, create_btn, create_btn_mrkup_services, create_btn_liquid_glass
from utils.dbmanage.dbcontrol import client_exists, add_client_to_db, delete_client, get_price_wash, get_price_polish, get_price_dry_cleaner, get_price_prot_cover, \
    get_price_liquid_glass
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

cars_types = {"sedan": "седан", "cross": "кроссовер", "vned": "внедорожник", "microbus": "микроавтобус"}

cars_service_types = {"moika_sedan": {1: "седан"}, "moika_cross": {2: "кроссовер"}, "moika_vned": {3: "внедорожник"}, "moika_microbus": {4: "микроавтобус"}}

cars_service_polish_types = {"polish_sedan": {1: "седан"}, "polish_cross": {2: "кроссовер"}, "polish_vned": {3: "внедорожник"}, "polish_microbus": {4: "микроавтобус"}}

cars_service_dry_cleaner_types = {"dry_cleaner_sedan": {1: "седан"}, "dry_cleaner_cross": {2: "кроссовер"}, "dry_cleaner_vned": {3: "внедорожник"}, 
                                  "dry_cleaner_microbus": {4: "микроавтобус"}}

cars_service_prot_cover_types = {"prot_cover_sedan": {1: "седан"}, "prot_cover_cross": {2: "кроссовер"}, "prot_cover_vned": {3: "внедорожник"}, 
                                  "prot_cover_microbus": {4: "микроавтобус"}}


@dp.callback_query_handler()
async def get_services_wash_car(callback: types.CallbackQuery):    
    if callback.data in cars_types.keys():
        await callback.message.answer(text=f"Выберите услугу для {cars_types.get(callback.data)}а", 
                                      reply_markup=create_btn_mrkup_services(callback.data))
    elif callback.data in cars_service_types.keys():
        await callback.message.answer(text=f"Цены на услугу МОЙКА {[v for v in cars_service_types.get(callback.data).values()][0]}а", 
                                      reply_markup=create_btn(get_price_wash([k for k in cars_service_types.get(callback.data).keys()][0])))
    elif callback.data in cars_service_polish_types.keys():
        await callback.message.answer(text=f"Цены на услугу ПОЛИРОВКА {[v for v in cars_service_polish_types.get(callback.data).values()][0]}а", 
                                      reply_markup=create_btn(get_price_polish([k for k in cars_service_polish_types.get(callback.data).keys()][0])))
    elif callback.data in cars_service_dry_cleaner_types.keys():
        await callback.message.answer(text=f"Цены на услугу ХИМЧИСТКА {[v for v in cars_service_dry_cleaner_types.get(callback.data).values()][0]}а", 
                                      reply_markup=create_btn(get_price_dry_cleaner([k for k in cars_service_dry_cleaner_types.get(callback.data).keys()][0])))
    elif callback.data in cars_service_prot_cover_types.keys():
        await callback.message.answer(text=f"Цены на услугу ЗАЩИТНЫЕ ПОКРЫТИЯ {[v for v in cars_service_prot_cover_types.get(callback.data).values()][0]}а", 
                                      reply_markup=create_btn(get_price_prot_cover([k for k in cars_service_prot_cover_types.get(callback.data).keys()][0])))
    elif callback.data == "liq_glass":
        await callback.message.answer(text=f"Жидкое стекло. \
                                \nПокрытие кузова жидким стеклом H-7 Glass Coating (SOFT99, Япония) – цена от {get_price_liquid_glass(3)} рублей.\
                                \nH7 жидкое стекло для автомобиля обеспечивает надежную защиту кузова от различных воздействий внешней среды: \
                                \nосадков (дождя, снега, града), грязи, морской воды, экстремальных перемен температуры, а так же абразивного воздействия.", parse_mode="HTML",
                                reply_markup=create_btn_liquid_glass("ЖИДКОЕ СТЕКЛО", get_price_liquid_glass(3), "liquid_glass"))
    elif callback.data == "presale":
        await callback.message.answer(text=f"Предпродажная подготовка.\
                                \nСпециалисты нашей компании проведут предпродажную подготовку Вашего автомобиля на высочайшем уровне уже сегодня так, \
                                \nчто завтра у Вас не будет отбоя от покупателей! \
                                \nЕсли вы решили продать свой автомобиль, ему необходимо придать товарный вид – провести предпродажную подготовку. \
                                \nТакая подготовка включает в себя целый комплекс действий, которые при незначительных денежных затратах могут повысить рыночную стоимость вашей машины. \
                                \nПредпродажная подготовка – цена от 10 000 рублей.", parse_mode="HTML",
                                reply_markup=create_btn_liquid_glass("ПРЕДПРОДАЖНАЯ ПОДГОТОВКА", 10000, "presale_back"))


@dp.message_handler(commands=['quit'])
async def delete_client(message: types.message):
    delete_client(message.from_user.id)
    await bot.send_message(message.from_user.id, text="Жаль, что вы нас покидаете. Мы ждем Вас снова.")


@dp.message_handler(commands=['location'])
async def info(message: types.message):
    await bot.send_message(message.from_user.id, text="Коломяжский пр., д. 19 (территория АЗС «ЛИНОС»)\nВыборгская наб., д. 57, лит. А (территория АЗС «ЛИНОС»).")
    
