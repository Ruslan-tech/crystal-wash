import os
from peewee import *


db = SqliteDatabase('crystal-db.db')


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
    

class SubservicePolish(BaseModel):
    title = CharField()


class SubserviceDryCleaner(BaseModel):
    title = CharField()


class SubserviceProtCover(BaseModel):
    title = CharField()
    
    
class CarClass(BaseModel):
    class_title = CharField()


class Price_wash(BaseModel):
    car_class_id = ForeignKeyField(CarClass)
    sub_serv_id = ForeignKeyField(Subservice)
    price = IntegerField()    
    comments = CharField(null=True)
    
    
class PricePolish(BaseModel):
    car_class_id = ForeignKeyField(CarClass)
    sub_serv_id = ForeignKeyField(SubservicePolish)
    price = IntegerField()    
    comments = CharField(null=True)
    
    
class PriceDryCleaner(BaseModel):
    car_class_id = ForeignKeyField(CarClass)
    sub_serv_id = ForeignKeyField(SubserviceDryCleaner)
    price = IntegerField()    
    comments = CharField(null=True)


class PriceProtCover(BaseModel):
    car_class_id = ForeignKeyField(CarClass)
    sub_serv_id = ForeignKeyField(SubserviceProtCover)
    price = IntegerField()    
    comments = CharField(null=True)
    
    
db.connect()
db.create_tables([Clients, Services, Subservice, SubservicePolish, SubserviceDryCleaner, 
                  SubserviceProtCover, CarClass, Price_wash, PricePolish, PriceDryCleaner, PriceProtCover])

