import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from app import ma, connect
from models import user, order


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


class CrepeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Crepe
        include_fk = True

    id = ma.auto_field()
    #toppings = ma.auto_field()
