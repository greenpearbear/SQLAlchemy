from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import all_function
import use_json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER, primary_key=True)
    first_name = db.Column(db.TEXT)
    last_name = db.Column(db.TEXT)
    age = db.Column(db.INTEGER)
    email = db.Column(db.TEXT)
    role = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)


class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    description = db.Column(db.TEXT)
    start_date = db.Column(db.TEXT)
    end_date = db.Column(db.TEXT)
    address = db.Column(db.TEXT)
    price = db.Column(db.INTEGER)
    customer_id = db.Column(db.INTEGER, db.ForeignKey('users.id'))
    user = db.relationship("Users")
    offer = db.relationship("Offers")


class Offers(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.INTEGER, primary_key=True)
    order_id = db.Column(db.INTEGER, db.ForeignKey('orders.id'))
    executor_id = db.Column(db.INTEGER, db.ForeignKey('users.id'))
    user = db.relationship("Users")


db.create_all()


def from_json_to_database():
    data_list = use_json.read_json('Users')
    for data in data_list:
        user = Users(id=data['id'], first_name=data['first_name'], last_name=data['last_name'],
                     age=data['age'], email=data['email'], role=data['role'], phone=data['phone'])
        db.session.add(user)
        db.session.commit()
    db.session.close()
    data_list = use_json.read_json('Orders')
    for data in data_list:
        user = Orders(id=data['id'], name=data['name'], description=data['description'],
                      start_date=data['start_date'], end_date=data['end_date'], address=data['address'],
                      price=data['price'], customer_id=data['customer_id'])
        db.session.add(user)
        db.session.commit()
    db.session.close()
    data_list = use_json.read_json('Offers')
    for data in data_list:
        user = Offers(id=data['id'], order_id=data['order_id'], executor_id=data['executor_id'])
        db.session.add(user)
        db.session.commit()
    db.session.close()


from_json_to_database()


@app.route('/users', methods=['GET', 'POST'])
def all_users():
    if request.method == 'GET':
        result = []
        users = Users.query.all()
        for user in users:
            result.append(all_function.return_request_user(user))
        return jsonify(result)
    if request.method == 'POST':
        data = request.json
        user = Users(first_name=data.get('first_name'),
                     last_name=data.get('last_name'),
                     age=data.get('age'),
                     email=data.get('email'),
                     role=data.get('role'),
                     phone=data.get('phone'))
        db.session.add(user)
        db.session.commit()
        db.session.close()
        return jsonify((all_function.return_request_user(user)))


@app.route('/users/<int:id_user>', methods=['GET', 'PUT', 'DELETE'])
def one_user(id_user):
    if request.method == 'GET':
        user = Users.query.get(id_user)
        return jsonify(all_function.return_request_user(user))
    if request.method == 'PUT':
        data = request.json
        user = Users.query.get(id_user)
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.age = data.get('age')
        user.email = data.get('email')
        user.role = data.get('role')
        user.phone = data.get('phone')
        db.session.add(user)
        db.session.commit()
        db.session.close()
    if request.method == 'DELETE':
        user = Users.query.get(id_user)
        db.session.delete(user)
        db.session.commit()
        db.session.close()

@app.route('/orders', methods=['GET'])
def all_orders():
    result = []
    orders = Orders.query.all()
    for order in orders:
        result.append(all_function.return_request_order(order))
    return jsonify(result)


@app.route('/orders/<int:id_order>', methods=['GET'])
def one_order(id_order):
    order = Orders.query.get(id_order)
    return jsonify(all_function.return_request_order(order))


@app.route('/offers', methods=['GET'])
def all_offers():
    result = []
    offers = Offers.query.all()
    for offer in offers:
        result.append(all_function.return_request_offer(offer))
    return jsonify(result)


@app.route('/orders/<int:id_offer>', methods=['GET'])
def one_offers(id_offer):
    offer = Offers.query.get(id_offer)
    return jsonify(all_function.return_request_user(offer))


if __name__ == "__main__":
    app.run()
