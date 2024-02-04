import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from marshmallow import fields, Schema
from models import user
from database.connect import connect


class Order(connect.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    note: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[str]
    user = relationship(user.User, backref="orders")
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

    def delete(self):
        connect.session.delete(self)
        connect.session.commit()

        return f"{self.name} deleted successfully"


class OrderSchema(Schema):
    class Meta:
        model = Order
        include_fk = True

    id = fields.Integer()
    name = fields.String()
    note = fields.String()
    status = fields.String()
    user = fields.Nested(user.UserSchema())
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())