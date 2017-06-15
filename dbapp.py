from peewee import *
import datetime

db = SqliteDatabase('students.db')

class Teacher(Model):
    id = PrimaryKeyField()
    name = CharField()
    grade =  IntegerField()
    
    class Meta:
        database = db

def initialize_db():
    db.connnect()
    db.create_tables([Teacher], safe=True)

initialize_db()

