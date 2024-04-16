from fastapi import APIRouter
from services import projects_services
from data.models import PROJECT_STATUS_NUMS
from common.responses import BadRequest

projects_router = APIRouter(prefix='/projects')


@projects_router.get('/')
def get_projects(
        name: str | None = None,
        limit: int | None = None,
        status: str | None = None
):

    if status and status.lower() not in PROJECT_STATUS_NUMS:
        return BadRequest('Wrong status! Expected: open or closed.')

    result = projects_services.get_all(name, limit, status)
    return result
