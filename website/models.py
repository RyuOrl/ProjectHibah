from . import db #dari folder yg sama, import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin): 
  id = db.Column(db.Integer, primary_key=True)
  # email = db.Column(db.String(150), unique=True, nullable=False) #ini mw dipake ap engga???
  username = db.Column(db.String(150), unique=True, nullable=False)
  password = db.Column(db.String(150), nullable=False)
  date_created = db.Column(db.DateTime(timezone=True), default=func.now()) 