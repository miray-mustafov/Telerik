from fastapi import APIRouter, Response
from pydantic import BaseModel
from PresentationLayer.data import Product, Category, products, categories


class CategoryResponseModel(BaseModel):
    category: Category
    products: list[Product]


categories_router = APIRouter(prefix='/categories')


@categories_router.get('/')
def get_categories():
    return [
        CategoryResponseModel(
            category=c,
            products=list(filter(lambda p: p.category_id == c.id, products)))
        for c in categories]


@categories_router.get('/{id}')
def get_category_by_name(id: int):
    category = next((c for c in categories if c.id == id), None)

    if category is None:
        return Response(status_code=404)
    else:
        return CategoryResponseModel(
            category=category,
            products=list(
                filter(lambda p: p.category_id == category.id, products)))


@categories_router.post('/')
def create_category(category: Category):
    max_id = max(c.id for c in categories)

    category.id = max_id + 1
    categories.append(category)

    return CategoryResponseModel(category=category, products=[])
