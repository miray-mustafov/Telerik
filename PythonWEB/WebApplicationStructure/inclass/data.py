from pydantic import BaseModel
from datetime import date

class Product(BaseModel):
    id: int | None
    name: str
    description: str
    price: float
    category_id: int


class Category(BaseModel):
    id: int | None
    name: str


class Order(BaseModel):
    id: int | None
    customer: str
    product_ids: list[int]
    delivery_date: date


categories = [
    Category(id=1, name='Computers and Accessories'),
    Category(id=2, name='Television'),
    Category(id=3, name='Cell Phones')
]

products = [
    Product(id=1, name='TV', description='LCD 40 Inch',
            price=749.99, category_id=2),
    Product(id=2, name='Laptop',
            description='2x2.6 GHz CPU; 6GB RAM; HD Graphics', price=699.99, category_id=1),
    Product(id=3, name='Smartphone', description='6.55" HD+, 5G',
            price=1349.90,  category_id=3),
    Product(id=4, name='Keyboard',
            description='Full-size Layout, Mechanical', price=99.00, category_id=1),
    Product(id=5, name='Improved Generic TV',
            description='Flat Screen, 720p', price=239.50, category_id=2),
    Product(id=6, name='Turbo Smartphone v2',
            description='48MP Camera, 128 GB', price=719.00, category_id=3),
    Product(id=7, name='Headphones',
            description='Black, Wireless', price=39.00, category_id=1)
]

orders = [
    Order(id = 1, customer='Steven', product_ids=[2,4], delivery_date=date(2025, 2, 8)),
    Order(id = 2, customer='Alice', product_ids=[1], delivery_date=date(2023, 8, 4))
]
