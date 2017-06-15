from flask import Flask, render_template, request
from peewee import *

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

app = Flask(__name__)

@app.route('/')
def home():
    return "Home"
    
    
@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method =='POST':
        age = request.form['age']
        
        return render_template('age.html', age=age)
        
    return render_template('index.html')
    


if __name__ =="__main__":
    app.run(debug=True)