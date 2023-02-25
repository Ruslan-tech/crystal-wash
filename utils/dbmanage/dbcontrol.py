from .models import Users, Position, Theeme, SheduleMasters, Profile
from py_log import *
import datetime


######################## users ###################################
def add_user_to_db(user_id: int) -> None:
    """save users in DB"""
    try:
        user = Users(user_tg_id=user_id)
        user.save()
    except Exception:
        logger.exception('error to add new user to database')


def user_exists(user_tg_id: int) -> bool:
    """return True if user exists"""
    try:
        query = Users.select().where(Users.user_tg_id == user_tg_id)
        master_ex = query.dicts().execute()
        return len([k for k in master_ex]) > 0
    except Exception as ex:
        logger.exception('error in searching for an existing user in the database', ex)
        
        
def get_user_id(user_tg_id: int) -> int:
    """return user id from db"""
    try:
        user_info = Users.select(Users.id).where(Users.user_tg_id == user_tg_id)
        user = user_info.dicts().execute()
        return [k for k in user][0]['id']
    except Exception:
        logger.exception("Can't get user name from database")
        

###################################


######################## position ###################################

def get_position(user_id: int) -> str:
    """return user position from DB"""
    try:
        query = Users.select().where(Users.user_tg_id == user_id)
        user_pos = query.dicts().execute()
        return [k for k in user_pos][0]['position']
    except Exception as ex:
        logger.exception('error in searching for an existing user in the database', ex)
        
        
###################################


######################## profile ###################################
def add_new_profile_to_db(fullname: str, user_id: int, position_id: int) -> None:
    """insert new profile for user to db"""
    try:
        profile = Profile(fullname=fullname, user_id=user_id, position_id=position_id)
        profile.save()
    except Exception:
        logger.exception("Can't create profile.")


def exists_profile(theeme_id: int, user_id: int):
    """return True if profile exists and False if not"""
    try:
        exist_prof = Profile.select().where((Profile.theeme_id == theeme_id) &
                                            (Profile.user_id == user_id))
        exist = exist_prof.dicts().execute()
        return len([prof for prof in exist]) > 0
    except Exception:
        logger.exception("Can't check exists profile.")
        

def get_profile(user_id: int):
    """return profile info from db"""
    try:
        profile = Profile.select().where(Profile.user_id == user_id)
        prof = profile.dicts().execute()
        return [prf for prf in prof]
    except Exception:
        logger.exception(f"Can't get profile for user {user_id}.")
        
        
###################################


######################## shedulemasters ###################################
def exsists_work_day(day: datetime.date, time_up: datetime.time, profiles_id: int) -> bool:
    """return True if work day exists for user or False if not"""
    try:
        exist_wd = SheduleMasters.select().where((SheduleMasters.day == day) &
                                                 (SheduleMasters.time_up ==time_up) &
                                                 (SheduleMasters.profiles_id == profiles_id))
        exist = exist_wd.dicts().execute()
        return len([day for day in exist]) > 0
    except Exception:
        logger.exception("")
    

def add_work_day_for_master(day: datetime.date, time_up: datetime.time, 
                            time_down: datetime.time, condition: str, profiles_id: int) -> None:
    """insert to db new work day for master shedule"""
    try:
        work_day = SheduleMasters(day=day, time_up=time_up, time_down=time_down, 
                                  condition=condition, profiles_id=profiles_id)
        work_day.save()
    except Exception:
        logger.exception("Can't add to db new work day for master shedule.")
        
        
###########################################