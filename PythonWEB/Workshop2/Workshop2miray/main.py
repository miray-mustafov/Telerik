from fastapi import FastAPI
from data.database import init_database
from routers.categories import categories_router
from routers.profiles import profiles_router
from routers.products import products_router
import uvicorn

init_database()

app = FastAPI()
app.include_router(categories_router)
app.include_router(products_router)
app.include_router(profiles_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)
