from fastapi import APIRouter, Query, Response
from fastapi.responses import JSONResponse
from services import devs_service
from data.models import Dev


devs_router = APIRouter(prefix='/devs')


@devs_router.get('/')
def get_devs(name: str | None = None,
             level: str | None = Query(default=None, regex='^junior|mid|senior$')):
    return devs_service.get_all(name, level)


@devs_router.get('/{id}')
def get_dev_by_id(id: int):
    project = devs_service.get_by_id(id)

    return project or Response(status_code=404)


@devs_router.post('/', status_code=201)
def create_project(dev: Dev):
    if devs_service.name_exists(dev.name):
        return JSONResponse(status_code=409, content={'detail': 'Dev name must be unique'})

    return devs_service.create(dev)
