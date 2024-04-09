from fastapi import APIRouter, Response
from pydantic import BaseModel
from BusinessLayer.data import Category, Product
from BusinessLayer.services import product_service
from BusinessLayer.services import category_service


class CategoryResponseModel(BaseModel):
    category: Category
    products: list[Product]


categories_router = APIRouter(prefix='/categories')


@categories_router.get('/')
def get_categories():
    return [
        CategoryResponseModel(
            category=c,
            products=product_service.get_by_category(c.id))
        for c in category_service.all()]


@categories_router.get('/{id}')
def get_category_by_name(id: int):
    category = category_service.get_by_id(id)

    if category is None:
        return Response(status_code=404)
    else:
        return CategoryResponseModel(
            category=category,
            products=product_service.get_by_category(category.id))


@categories_router.post('/')
def create_category(category: Category):
    created_category = category_service.create(category)

    return CategoryResponseModel(category=created_category, products=[])
