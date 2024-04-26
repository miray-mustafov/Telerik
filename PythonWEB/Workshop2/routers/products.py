from fastapi import APIRouter
from data.models import Product, INITIAL_INTEREST
from services import products_services, interests_services, profiles_services
from common.responses import BadRequest

products_router = APIRouter(prefix='/products', tags=['products'])


@products_router.put('/{product_id}/profiles/{profile_id}')
def view_product_by_profile_id_product_id(product_id: int, profile_id: int):
    product = products_services.get_by_id(product_id)
    if not product:
        return BadRequest('No such product')
    if not profiles_services.profile_exists(profile_id):
        return BadRequest('No such profile')

    is_new_profile_interest_added = interests_services.add_profile_category_pair(profile_id, product.category_id)
    interest = INITIAL_INTEREST
    if not is_new_profile_interest_added:
        interest = interests_services.update_profile_category_interest(profile_id, product.category_id)

    return product, {"interest": interest}
