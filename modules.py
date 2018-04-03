#encoding: utf-8

from exits import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100), nullable=False)



class Car_rental(db.Model):
    __tablename__ = 'car_rental'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    author_id=db.Column(db.Integer,db.ForeignKey('user.id'))

    author = db.relationship('User',backref =db.backref('car_rental'))


class Cars(db.Model):
    __tablename__ = 'Cars'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    location=db.Column(db.String(100),nullable=False)
    Bdatetime=db.Column(db.Text,nullable=False)
    Bday = db.Column(db.Text, nullable=False)
    Btime = db.Column(db.Text, nullable=False)
    Rdatetime = db.Column(db.Text, nullable=False)
    Rday = db.Column(db.Text, nullable=False)
    Rtime = db.Column(db.Text, nullable=False)

    create_time = db.Column(db.DateTime,default=datetime.now)
    cattype=db.Column(db.String(100),nullable=False)
    gearbox=db.Column(db.String(100),nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('Cars'))



class CarsDataset(db.Model):
    __tablename__ = 'CarsDataset'

    name=db.Column(db.Text,nullable=False)
    price=db.Column(db.Integer,nullable=False)
    vehicleType = db.Column(db.Text, nullable=False)
    yearOfRegistration = db.Column(db.Integer, nullable=False)
    gearbox = db.Column(db.Text, nullable=False)
    kilometer = db.Column(db.Integer, nullable=False)
    brand= db.Column(db.Text, nullable=False)
    lng=db.Column(db.Float,nullable=False)
    lat=db.Column(db.Float,nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)

    author = db.relationship('User', backref=db.backref('CarsDataset'))





