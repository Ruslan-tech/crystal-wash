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


db.connect()
db.create_tables([Clients])
