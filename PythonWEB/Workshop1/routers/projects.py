from fastapi import APIRouter
from services import projects_services
from data.models import Project, PROJECT_STATUS_NUMS, ProjectStatusUpdate
from common.responses import BadRequest, NotFound

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


@projects_router.get('/{id}')
def get_project_by_id(id: int):
    result = projects_services.get_by_id(id)
    if not result:
        return NotFound()
    return result


@projects_router.post('/', status_code=201)
def create_project(project: Project):
    result = projects_services.create(project)
    return result


@projects_router.put('/{id}')
def update_project(id: int, status_obj: ProjectStatusUpdate):
    existing_project = projects_services.get_by_id(id)
    if not existing_project:
        return BadRequest(f'No project with id: {id}!')
    result = projects_services.update(existing_project, status_obj)
    return result

# use with caution bcs the devs_projects table
# @projects_router.delete('/{id}', status_code=204)
# def delete_project(id):
#     projects_services.delete(id)
