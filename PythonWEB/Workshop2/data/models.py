from pydantic import BaseModel

INTEREST_INCREASE_PERCENTAGE = 5
INITIAL_INTEREST = 1


class Interest(BaseModel):
    interest: int


class Profile(BaseModel):
    id: int | None = None
    ip_address: str
    country_code: str


class Category(BaseModel):
    id: int | None = None
    name: str


class Product(BaseModel):
    id: int | None = None
    name: str
    price: float
    category_id: int

    @classmethod
    def from_query_result(cls, id, name, price, category_id):
        return cls(
            id=id,
            name=name,
            price=price,
            category_id=category_id
        )

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
