from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    first_name = db.Column(db.TEXT)
    last_name = db.Column(db.TEXT)
    age = db.Column(db.INTEGER)
    email = db.Column(db.TEXT)
    role = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    orders = db.relationship("Orders")
    offers = db.relationship("Offers")


class Orders(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    description = db.Column(db.TEXT)
    star_date = db.Column(db.DATE)
    end_date = db.Column(db.DATE)
    address = db.Column(db.TEXT)
    price = db.Column(db.INTEGER)
    customer_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))
    user = db.relationship("Users")
    offer = db.relationship("Offers")


class Offers(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    order_id = db.Column(db.INTEGER, db.ForeignKey('order.id'))
    executor_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))
    user = db.relationship("Users")
    orders = db.relationship("Orders")
