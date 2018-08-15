# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from flask import *
from sqlalchemy import *
from flask_sqlalchemy import *
import psycopg2
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pucit123@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
class students(db.Model):
    #auto increament krta student_id
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin




f=students(name="wajahat",city="falcon",addr="faisal twn",pin="123")

db.session.add(f)

#select * from students
T=f.query.all()
#imprtant for inserting 
db.session.commit()

for result in T:
    print(result.name,result.city)

print(T)