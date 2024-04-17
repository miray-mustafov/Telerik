from fastapi import APIRouter
from services import devs_services, projects_services
from data.models import Developer, DEV_LEVELS, Status, Seniority
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

    if devs_services.already_assigned_to_that_project(dev_id, project_id):
        return BadRequest('Dev already assigned to that project')

    if not devs_services.can_assign_that_dev(dev):
        return BadRequest('That Nonsenior dev already has project to work on')

    if (dev.level_str != Seniority.SENIOR and
            projects_services.will_reach_limit_without_a_senior(project)):
        return BadRequest('Project must have at least one senior')

    result = devs_services.assign_project(dev_id, project_id)
    if result == dev_id:
        return f'Dev {dev_id} {dev.name} assigned to project {project_id} {project.name}'
    return result


@devs_router.delete('/{dev_id}/projects/{project_id}')
def remove_dev_from_project(dev_id: int, project_id: int):
    if not devs_services.get_by_id(dev_id):
        return BadRequest("No such dev")

    if not projects_services.get_by_id(project_id):
        return BadRequest("No such project")

    is_deleted = devs_services.remove_from_project(dev_id, project_id)
    if is_deleted:
        return f'Dev with id: {dev_id} is no longer in project with id: {project_id}'
    return is_deleted

# use with caution bcs the devs_projects table
# @devs_router.delete('/{id}', status_code=204)
# def delete_dev(id):
#     devs_services.delete(id)
