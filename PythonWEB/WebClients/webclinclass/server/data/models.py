from datetime import date
from pydantic import BaseModel, constr


class Category(BaseModel):
    id: int | None = None
    name: str


class Product(BaseModel):  # modified
    id: int | None = None
    name: str
    description: str
    price: float
    category_id: int | None = None

    @classmethod
    def from_query_result(cls, id, name, description, price, category_id):
        return cls(
            id=id,
            name=name,
            description=description,
            price=price,
            category_id=category_id)



class Order(BaseModel):  # modified
    id: int | None = None
    product_ids: list[int] = []
    delivery_date: date
    delivery_address: str | None = None
    user_id: int

    @classmethod
    def from_query_result(cls, id, delivery_date, delivery_address, user_id=None, product_ids=[]):
        return cls(
            id=id,
            delivery_date=delivery_date,
            delivery_address=delivery_address,
            user_id=user_id,
            product_ids=product_ids)


class OrderUpdate(BaseModel):
    delivery_date: date
    delivery_address: str


class Role:
    CUSTOMER = 'customer'
    ADMIN = 'admin'


TUsername = constr(pattern=r'^\w{2,30}$')


class User(BaseModel):
    id: int | None = None
    username: TUsername
    password: str
    role: str

    def is_admin(self):
        return self.role == Role.ADMIN

    @classmethod
    def from_query_result(cls, id, username, password, role):
        return cls(
            id=id,
            username=username,
            password=password,
            role=role)


class LoginData(BaseModel):
    username: TUsername
    password: str


class UserResponse(BaseModel):
    id: int | None = None
    username: str


class OrderResponse(BaseModel):
    id: int | None = None
    customer: UserResponse
    products: list[Product]
    delivery_date: date
    delivery_address: str
    order_total: float
