from pydantic import BaseModel


class Profile(BaseModel):
    id: int | None = None
    ip_address: str
    country_code: str


# class CategoryRelevance(BaseModel):
#     id: int | None = None
#     name: str
#     relevance: int
#
#
# class ProfileExtended(BaseModel):
#     id: int | None = None
#     ip_address: str
#     country_code: str
#     categories = list[CategoryRelevance]


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
