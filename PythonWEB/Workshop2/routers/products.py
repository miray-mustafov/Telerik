from fastapi import APIRouter
from data.models import Product
from services import products_services
from common.responses import BadRequest

products_router = APIRouter(prefix='/products', tags=['products'])


@products_router.get('/')
def get_all_products():
    products = products_services.get_all()
    return products
