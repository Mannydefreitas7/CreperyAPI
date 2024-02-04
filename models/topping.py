import datetime
from sqlalchemy import Column, DateTime, Boolean, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship
from marshmallow import post_load, fields, Schema
from database.connect import connect
from models import crepe


class Topping(connect.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    calories: Mapped[str]
    image_data: Mapped[bytes]
    crepe_id: Mapped[int] = mapped_column(ForeignKey("crepe.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, topping_id):
        return cls.query.get_or_404(topping_id)

    def save(self):
        connect.session.add(self)
        connect.session.commit()

    def delete(self):
        connect.session.delete(self)
        connect.session.commit()


class ToppingSchema(Schema):
    class Meta:
        model = Topping

    id = fields.Integer()
    name = fields.String()
    calories = fields.String()
    image_data = fields.String()
    created_at = fields.DateTime()

    @post_load
    def make_topping(self, data, **kwargs):
        return Topping(**data)

