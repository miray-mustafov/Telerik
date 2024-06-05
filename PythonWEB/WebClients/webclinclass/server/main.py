from fastapi import FastAPI
from routers.product import product_router
from routers.categories import categories_router
from routers.orders import orders_router
from routers.users import users_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=[
        "http://localhost:8001",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)
app.include_router(categories_router)
app.include_router(orders_router)
app.include_router(users_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8001)