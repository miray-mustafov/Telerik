from fastapi import APIRouter
from services import projects_services

projects_router = APIRouter(prefix='/projects')


@projects_router.get('/')
def get_projects(
        name: str | None = None,
        limit: int | None = None,
        status: str | None = None
):
    result = projects_services.all(name, limit, status)
    return result
