from fastapi import APIRouter
from data.models import Profile
from services import profiles_services
from common.responses import BadRequest

profiles_router = APIRouter(prefix='/profiles', tags=['profiles'])


@profiles_router.get('/')
def get_all_profiles(country_code: str | None = None):
    profiles = profiles_services.get_all(country_code)
    return profiles


@profiles_router.get('/country_codes')
def get_all_country_codes():
    country_codes = profiles_services.get_all_country_codes()
    return country_codes
