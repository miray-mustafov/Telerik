from fastapi import FastAPI
from data.database import init_database
from routers.devs import devs_router
from routers.projects import projects_router
import uvicorn

init_database()

app = FastAPI()
app.include_router(devs_router)
app.include_router(projects_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)
