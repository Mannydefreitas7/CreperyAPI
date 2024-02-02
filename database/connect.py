from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


connect = SQLAlchemy(model_class=Base)

if __name__ == '__main__':
    connect = SQLAlchemy(model_class=Base)
