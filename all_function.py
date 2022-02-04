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


