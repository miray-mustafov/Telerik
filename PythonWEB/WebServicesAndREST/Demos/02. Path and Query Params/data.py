from pydantic import BaseModel

class Product(BaseModel):
    id: int | None
    name: str
    description: str
    price: float


data = [
    Product(id=1, name='TV', description='LCD 40 Inch', price = 749.99),
    Product(id=2, name='Laptop', description='2x2.6 GHz CPU; 6GB RAM; HD Graphics', price = 699.99),
    Product(id=3, name='Smartphone', description='6.55" HD+, 5G', price = 1349.90),
    Product(id=4, name='Keyboard', description='Full-size Layout, Mechanical', price = 99.00),
]