from datetime import date
from pydantic import BaseModel, constr


class Category(BaseModel):
    id: int | None
    name: str


class Product(BaseModel):
    id: int | None
    name: str
    description: str
    price: float
    category_id: int

    @classmethod
    def from_query_result(cls, id, name, description, price, category_id):
        return cls(
            id=id,
            name=name,
            description=description,
            price=price,
            category_id=category_id)


class Order(BaseModel):
    id: int | None
    product_ids: list[int] = []
    delivery_date: date
    user_id: int or None  # todo
    delivery_address: str | None

    @classmethod
    def from_query_result(cls, id, delivery_date, delivery_address, user_id, product_ids=[]):
        return cls(
            id=id,
            delivery_date=delivery_date,
            delivery_address=delivery_address,
            user_id=user_id,
            product_ids=product_ids
        )


class OrderUpdate(BaseModel):
    delivery_date: date
    delivery_address: str | None


TUsername = constr(pattern=r'^\w{2,30}$')


class User(BaseModel):
    id: int | None
    username: TUsername
    password: str
    role: str
    order_ids: list[int] = []

    def is_admin(self):
        return self.role == 'Admin'

    @classmethod
    def from_query_result(cls, id, username, password, role, order_ids=[]):
        return cls(
            id=id,
            username=username,
            password=password,
            role=role,
            order_ids=order_ids
        )



class LoginData(BaseModel):
    username: TUsername
