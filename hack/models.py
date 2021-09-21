import sqlite3 as sql
from os import path 
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    posted = db.Column(db.String(100))
    author = db.Column(db.String(1000))
    author_id = db.Column(db.Integer)
    title = db.Column(db.String(100))
    content = db.Column(db.String(1000))

