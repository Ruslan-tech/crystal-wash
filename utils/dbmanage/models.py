import os
from peewee import *


db = PostgresqlDatabase('crystal-db', user='postgres', password='crystal23',
                           host='localhost', port=5433)


class BaseModel(Model):
    class Meta:
        database = db


class Clients(BaseModel):
    user_tg_id = IntegerField()
    user_name = CharField(max_length=50)


class Services(BaseModel):
    title = CharField(max_length=80)
    
    
class Cars(BaseModel):
    mark = CharField()
    model = CharField()
    color =  CharField(max_length=15)
    num = CharField(max_length=10)


class Client_Cars(BaseModel):
    user_id = ForeignKeyField(Clients)
    cars_id = ForeignKeyField(Cars)


class Subservice(BaseModel):
    title = CharField()
    

class CarClass(BaseModel):
    class_title = CharField()

class Price(BaseModel):
    pass
    

db.connect()
db.create_tables([Clients, Services, Subservice, CarClass])

