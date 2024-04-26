from fastapi import FastAPI
from data.database import init_database

init_database()

app = FastAPI()
