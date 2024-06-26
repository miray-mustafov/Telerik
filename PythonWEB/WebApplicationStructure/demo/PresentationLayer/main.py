from fastapi import FastAPI
from routers.product import product_router
from routers.categories import categories_router


app = FastAPI()
app.include_router(product_router)
app.include_router(categories_router)
