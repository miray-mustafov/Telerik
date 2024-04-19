from typing import Annotated
from fastapi import APIRouter, Body, Query, Response
from fastapi.responses import JSONResponse
from services import projects_service, devs_service
from data.models import Project


projects_router = APIRouter(prefix='/projects')


@projects_router.get('/')
def get_projects(name: str | None = None,
                 limit: int | None = None,
                 status: str | None = Query(default=None, regex='^open|closed$')):
    return projects_service.get_all(name, limit, status)


@projects_router.get('/{id}')
def get_project_by_id(id: int):
    project = projects_service.get_by_id(id)

    return project or Response(status_code=404)


@projects_router.post('/', status_code=201)
def create_project(project: Project):
    if projects_service.name_exists(project.name):
        return JSONResponse(status_code=409, content={'detail': 'Project name must be unique'})

    return projects_service.create(project)


@projects_router.put('/{id}/status')
def set_status(id: int, status: str = Body(embed=True, regex='^open|closed$')):
    if not projects_service.id_exists(id):
        return Response(status_code=404)

    projects_service.set_status(id, status)

    return {'message': f'Status set to {status}.'}


@projects_router.post('/{project_id}/devs/{dev_id}')
def assign_to_project(project_id: int, dev_id: int):
    if not projects_service.id_exists(project_id):
        return JSONResponse(
            status_code=404,
            content={'detail': f'No project with id {project_id}'})

    if not devs_service.id_exists(dev_id):
        return JSONResponse(
            status_code=404,
            content={'detail': f'No dev with id {dev_id}'})

    ok, description = projects_service.assign_to_project(project_id, dev_id)

    return JSONResponse(
        status_code=200 if ok else 409,
        content={'message' if ok else 'detail': description})

@projects_router.delete('/{project_id}/devs/{dev_id}')
def assign_to_project(project_id: int, dev_id: int):
    if not projects_service.id_exists(project_id):
        return JSONResponse(
            status_code=404,
            content={'detail': f'No project with id {project_id}'})

    if not devs_service.id_exists(dev_id):
        return JSONResponse(
            status_code=404,
            content={'detail': f'No dev with id {dev_id}'})

    ok, description = projects_service.remove_from_project(project_id, dev_id)

    return JSONResponse(
        status_code=200 if ok else 409,
        content={'message' if ok else 'detail': description})
