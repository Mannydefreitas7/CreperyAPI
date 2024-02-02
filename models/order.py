import datetime
from sqlalchemy import Column, DateTime, Boolean, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import ma, connect
from models.user import User


class Order(connect.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    note: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[str]
    user = relationship(User, backref="orders")
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())


class OrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Order
        include_fk = True


    # crepes = ma.auto_field()
