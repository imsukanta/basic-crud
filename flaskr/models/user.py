from flaskr import db
from sqlalchemy import Integer,String
class User(db.Model):
    __tablename__="users"
    id=db.Column(Integer,primary_key=True)
    first_name=db.Column(String(50))
    last_name=db.Column(String(50))
    email=db.Column(String(50),unique=True)
    roll_no=db.Column(String(100))