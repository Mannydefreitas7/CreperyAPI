# app.py
import os
from flask import Flask, request, jsonify, Request
from flask_marshmallow import Marshmallow
from flask_pyjwt import AuthManager
from dotenv import load_dotenv
from urllib import request as req
import certifi

from database.connect import connect
from models.user import *
from models.topping import *
from models.order import *
from models.crepe import *

load_dotenv()

app = Flask(__name__)
auth_manager = AuthManager(app)
url = os.getenv("DATABASE_URL")
whoami_url = os.getenv("WHOAMI_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = url

connect.init_app(app)
ma = Marshmallow(app)


try:
    with app.app_context():
        connect.create_all()
except Exception as error:
    print(error)


@app.get("/api/login")
def login():
    response = req.urlopen(whoami_url, cafile=certifi.where())
    type: str = response.headers['Content-Type']
    if 'html' in type:
        return response.read()
    elif 'json' in type:
        return "test"


@app.get("/api/users")
def get_users():
    users = User.get_all()
    serializer = UserSchema(many=True)
    data = serializer.dump(users)
    return jsonify(
        data
    )


@app.post("/api/users")
def post_user():
    data = request.get_json()
    serializer = UserSchema()
    result = serializer.load(data)
    id = User.save(result)
    return (
        jsonify(
            message="Success",
            id=id
        )
    )


@app.put("/api/users/<int:user_id>")
def put_user(user_id):
    data = request.get_json()
    serializer = UserSchema()
    result = serializer.load(data)
    user = User.update(result, user_id)
    return (
        jsonify(
            message="Success",
            id=user.id
        )
    )


@app.delete("/api/users/<int:user_id>")
def delete_user(user_id):
    user = connect.session.get(User, user_id)
    message = User.delete(user)

    return (
        jsonify(
            message=message
        )
    )


@app.get("/api/toppings")
def get_toppings():
    toppings = Topping.get_all()
    serializer = ToppingSchema(many=True)
    data = serializer.dump(toppings)
    return jsonify(
        data
    )


@app.post("/api/toppings")
def post_topping():
    data = request.get_json()
    serializer = ToppingSchema()
    result = serializer.load(data)
    id = Topping.save(result)
    return (
        jsonify(
            message="Success",
            id=id
        )
    )


@app.put("/api/toppings/<int:topping_id>")
def put_topping(topping_id):
    data = request.get_json()
    serializer = ToppingSchema()
    result = serializer.load(data)
    topping = Topping.update(result, topping_id)
    return (
        jsonify(
            message="Success",
            id=topping.id
        )
    )


@app.delete("/api/toppings/<int:topping_id>")
def delete_topping(topping_id):
    topping = connect.session.get(Topping, topping_id)
    message = Topping.delete(topping)

    return (
        jsonify(
            message=message
        )
    )


@app.get("/api/orders")
def get_orders():
    orders = Order.get_all()
    serializer = OrderSchema(many=True)
    data = serializer.dump(orders)
    return jsonify(
        data
    )


@app.post("/api/orders")
def post_order():
    data = request.get_json()
    serializer = OrderSchema()
    result = serializer.load(data)
    id = Order.save(result)
    return (
        jsonify(
            message="Success",
            id=id
        )
    )


@app.put("/api/orders/<int:order_id>")
def put_order(order_id):
    data = request.get_json()
    serializer = OrderSchema()
    result = serializer.load(data)
    payload = Order.update(result, order_id)
    return (
        jsonify(
            message="Success",
            id=payload.id
        )
    )


@app.delete("/api/orders/<int:order_id>")
def delete_order(order_id):
    payload = connect.session.get(Order, order_id)
    message = Order.delete(payload)

    return (
        jsonify(
            message=message
        )
    )


@app.get("/api/crepes")
def get_crepes():
    crepes = Crepe.get_all()
    serializer = CrepeSchema(many=True)
    data = serializer.dump(crepes)
    return jsonify(
        data
    )


@app.post("/api/crepes")
def post_crepe():
    data = request.get_json()
    serializer = CrepeSchema()
    result = serializer.load(data)
    id = Crepe.save(result)
    return (
        jsonify(
            message="Success",
            id=id
        )
    )


@app.put("/api/crepes/<int:crepe_id>")
def put_crepe(crepe_id):
    data = request.get_json()
    serializer = CrepeSchema()
    result = serializer.load(data)
    payload = Crepe.update(result, crepe_id)
    return (
        jsonify(
            message="Success",
            id=payload.id
        )
    )


@app.delete("/api/crepes/<int:crepe_id>")
def delete_crepe(crepe_id):
    payload = connect.session.get(Crepe, crepe_id)
    message = Crepe.delete(payload)

    return (
        jsonify(
            message=message
        )
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
