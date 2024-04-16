from fastapi import APIRouter
from services import devs_services
from data.models import DEV_LEVELS
from common.responses import BadRequest

devs_router = APIRouter(prefix='/devs')


@devs_router.get('/')
def get_projects(
        name: str | None = None,
        level_str: str | None = None
):
    if level_str and level_str.lower() not in DEV_LEVELS:
        return BadRequest('Wrong seniority level. Expected: junior, mid or senior.')

    result = devs_services.get_all(name, level_str)
    return result


@devs_router.get('/{id}')
def get_dev_by_id(id: int):
    result = devs_services.get_by_id(id)
    return result
