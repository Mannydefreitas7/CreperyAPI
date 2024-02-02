# app.py
import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from database.connect import connect
from models import *

load_dotenv()


app = Flask(__name__)
url = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = url

connect.init_app(app)
ma = Marshmallow(app)

try:
    with app.app_context():

        connect.create_all()
        print("created")
except Exception as error:
    print(error)
    print("error")


@app.get("/api/users")
def get_users():
    # data = request.get_json()
    return {"test": "load"}


@app.post("/api/users")
def post_user():
    # data = request.get_json()
    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
