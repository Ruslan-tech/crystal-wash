from .models import Clients
from py_log import *
import datetime


######################## clients ###################################
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
        print(query)
        # master_ex = query.dicts().execute()
        return query > 0
    except Exception as ex:
        logger.exception('error in searching for an existing user in the database', ex)
        
        
# def get_user_id(user_tg_id: int) -> int:
#     """return user id from db"""
#     try:
#         user_info = Users.select(Users.id).where(Users.user_tg_id == user_tg_id)
#         user = user_info.dicts().execute()
#         return [k for k in user][0]['id']
#     except Exception:
#         logger.exception("Can't get user name from database")
        

###################################

