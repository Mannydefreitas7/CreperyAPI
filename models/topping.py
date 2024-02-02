import datetime
from sqlalchemy import Column, DateTime, Boolean, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import ma, connect
from models import crepe


class Topping(connect.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    calories: Mapped[str]
    image_data: Mapped[bytes]
    crepe_id: Mapped[int] = mapped_column(ForeignKey("crepe.id"))
    crepe = relationship(crepe.Crepe, backref="toppings")
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())


class ToppingSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Topping

