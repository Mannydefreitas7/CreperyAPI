import datetime
from typing import List

from sqlalchemy import Column, DateTime, Boolean, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, foreign, relationship
from app import ma, connect


class User(connect.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    image_data: Mapped[bytes]
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        include_fk = True

   # crepes = ma.auto_field()
   # orders = ma.auto_field()