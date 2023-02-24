#install peewee
from peewee import *
from os import path

connectin = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connectin,"Emobilis.db"))

#creatin our table
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db

User.create_table(fail_silently=True)

