from fastapi import APIRouter
from data.models import Category
from services import categories_services
from common.responses import BadRequest

categories_router = APIRouter(prefix='/categories', tags=['categories'])

# @categories_router.get('/')
# def get_all_categories():
#     categories = categories_services.get_all()
#     return categories
