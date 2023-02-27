from .models import Clients, Price_wash, CarClass, Subservice
from py_log import *
import datetime


def add_client_to_db(user_id: int, user_name: str) -> None:
    """save users in DB"""
    try:
        user = Clients(user_tg_id=user_id, user_name=user_name)
        user.save()
    except Exception:
        logger.exception('error to add new user to database')


def client_exists(user_tg_id: int) -> bool:
    """return True if user exists"""
    try:
        query = Clients.select().where(Clients.user_tg_id == user_tg_id).count()
        return query > 0
    except Exception as ex:
        logger.exception('error in searching for an existing user in the database', ex)
        

def delete_client(user_tg_id: int) -> None:
    """delete user from db"""
    delite = Clients.delete().where(Clients.user_tg_id == user_tg_id)
    delite.execute()
    
    
def get_price_wash(car_class: int):
    """Get price for service"""
    query = Price_wash.select(Subservice.title, Price_wash.price).join(Subservice).where(Price_wash.car_class_id == car_class)
    pr = query.dicts().execute()
    [print(p['title'] + " - " + str(p['price']) + " rub") for p in pr]
    return [p for p in pr]


