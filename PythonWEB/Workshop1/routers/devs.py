from fastapi import APIRouter
from services import devs_services, projects_services
from data.models import Developer, DEV_LEVELS, Status
from common.responses import BadRequest, NotFound

devs_router = APIRouter(prefix='/devs')


@devs_router.get('/')
def get_devs(
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
    if not result:
        return NotFound()
    return result


@devs_router.post('/', status_code=201)
def create_dev(dev: Developer):
    result = devs_services.create(dev)
    return result


@devs_router.post('/{dev_id}/projects/{project_id}')
def assign_dev_to_project(dev_id: int, project_id: int):
    dev = devs_services.get_by_id(dev_id)
    if not dev:
        return BadRequest("No such dev")

    project = projects_services.get_by_id(project_id)
    if not project:
        return BadRequest("No such project")

    if Status.CLOSED == project.status:
        return BadRequest('Project is closed')

    if projects_services.is_team_limit_reached(project):
        return BadRequest("Project limit reached")

    
    # result = devs_services.assign_project(dev, project)
    return "Hi"


@devs_router.delete('/{id}', status_code=204)
def delete_dev(id):
    devs_services.delete(id)
