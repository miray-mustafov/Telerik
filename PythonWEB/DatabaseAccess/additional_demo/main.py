from fastapi import FastAPI
from routers.artists import artists_router
import uvicorn


app = FastAPI()

app.include_router(artists_router)

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8001)
