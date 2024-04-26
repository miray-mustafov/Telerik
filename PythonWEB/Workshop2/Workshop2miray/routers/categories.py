from fastapi import APIRouter
from data.models import Category
from services import categories_services

categories_router = APIRouter(prefix='/categories', tags=['categories'])


@categories_router.get('/')
def get_all_categories(country_code: str | None = None):
    categories = categories_services.get_all(country_code)
    return categories
