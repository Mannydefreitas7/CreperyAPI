import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from app import ma
from database.connect import connect
from models import user, order, topping
from marshmallow import post_load, fields


class Crepe(connect.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    calories: Mapped[str]
    image_data: Mapped[bytes]
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    user = relationship(user.User, backref="crepes")
    topping_id = mapped_column(ForeignKey("topping.id"))
    order = relationship(order.Order, backref="crepes")

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

    def update(self, id):
        self.id = id
        payload = connect.session.merge(self)
        connect.session.commit()

        return payload

    def delete(self):
        connect.session.delete(self)
        connect.session.commit()

        return f"{self.name} deleted successfully"


class CrepeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Crepe
        include_fk = True

    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    calories = fields.String()
    is_admin = fields.Boolean()
    image_data = fields.String()
    topping = fields.List(
        fields.Nested(topping.ToppingSchema())
    )
    created_at = fields.DateTime()
