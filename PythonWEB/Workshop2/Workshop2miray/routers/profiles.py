from fastapi import APIRouter
from common.responses import NotFound
from data.models import Profile
from services import profiles_services

profiles_router = APIRouter(prefix='/profiles', tags=['profiles'])


@profiles_router.get('/')
def get_all_profiles(country_code: str | None = None):
    profiles = profiles_services.get_all(country_code)
    return profiles


@profiles_router.get('/country_codes')
def get_all_country_codes():
    country_codes = profiles_services.get_all_country_codes()
    return country_codes


@profiles_router.get('/{id}')
def get_profile_by_id(id: int):
    profile = profiles_services.get_by_id_with_categories(id)
    if not profile:
        return NotFound()
    return profile
