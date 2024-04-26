from pydantic import BaseModel


class Profile(BaseModel):
    id: int | None = None
    ip_address: str
    country_code: str


class Category(BaseModel):
    id: int | None = None
    name: str


class Interest(BaseModel):
    pass


class Product(BaseModel):
    id: int | None = None
    name: str
    price: float
    category_id: int
