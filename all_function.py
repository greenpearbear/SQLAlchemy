import flask_SQLAlchemy
import use_json


def return_request_user(table):
    return {
        "id": table.id,
        "first_name": table.first_name,
        "last_name": table.last_name,
        "age": table.age,
        "email": table.email,
        "role": table.role,
        "phone": table.phone}


def return_request_order(table):
    return {
        "id": table.id,
        "name": table.name,
        "description": table.description,
        "start_date": table.start_date,
        "end_date": table.end_date,
        "address": table.address,
        "price": table.price,
        "customer_id": table.customer_id}


def return_request_offer(table):
    return {
        "id": table.id,
        "order_id": table.order_id,
        "executor_id": table.executor_id}


def from_json_to_database():
    data_list = use_json.read_json('Users')
    for data in data_list:
        user = flask_SQLAlchemy.Users(id=data['id'], first_name=data['first_name'], last_name=data['last_name'],
                                      age=data['age'], email=data['email'], role=data['role'], phone=data['phone'])
        flask_SQLAlchemy.db.session.add(user)
        flask_SQLAlchemy.db.session.commit()
    flask_SQLAlchemy.db.session.close()
    data_list = use_json.read_json('Orders')
    for data in data_list:
        user = flask_SQLAlchemy.Users(id=data['id'], name=data['name'], description=data['description'],
                                      star_date=data['star_date'], end_date=data['end_date'], address=data['address'],
                                      price=data['price'], customer_id=data['customer_id'])
        flask_SQLAlchemy.db.session.add(user)
        flask_SQLAlchemy.db.session.commit()
    flask_SQLAlchemy.db.session.close()
    data_list = use_json.read_json('Offers')
    for data in data_list:
        user = flask_SQLAlchemy.Users(id=data['id'], order_id=data['order_id'], executor_id=data['executor_id'])
        flask_SQLAlchemy.db.session.add(user)
        flask_SQLAlchemy.db.session.commit()
    flask_SQLAlchemy.db.session.close()
