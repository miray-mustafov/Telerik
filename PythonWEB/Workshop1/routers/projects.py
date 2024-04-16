from fastapi import APIRouter
from services import projects_services
from data.models import PROJECT_STATUS
from common.responses import BadRequest

projects_router = APIRouter(prefix='/projects')


@projects_router.get('/')
def get_projects(
        name: str | None = None,
        limit: int | None = None,
        status: str | None = None
):

    if status and status not in PROJECT_STATUS:
        BadRequest('Wrong status! Choose open or closed.')

    result = projects_services.get_all(name, limit, status)
    return result
