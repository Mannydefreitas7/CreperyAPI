import datetime
from typing import List

from sqlalchemy import Column, DateTime, Boolean, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, foreign, relationship
from flask_marshmallow import Schema
from marshmallow import post_load, fields
from database.connect import connect
import jwt


class User(connect.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(unique=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    image_data: Mapped[bytes] = mapped_column(nullable=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    def save(self):
        connect.session.add(self)
        connect.session.commit()
        return self.id

    def update(self, user_id):
        self.id = user_id
        user = connect.session.merge(self)
        connect.session.commit()

        return user

    def delete(self):
        connect.session.delete(self)
        connect.session.commit()

        return "Successfully Deleted"

    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.now() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.now(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e


class UserSchema(Schema):
    class Meta:
        model = User
        include_fk = True

    user_name = fields.String()
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    is_admin = fields.Boolean()
    image_data = fields.String()
    order_id = fields.Integer()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

   # crepes = ma.auto_field()
   # orders = ma.auto_field()