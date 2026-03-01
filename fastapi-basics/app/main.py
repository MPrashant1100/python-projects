from fastapi import FastAPI
from app.routes import expenses

app = FastAPI()

app.include_router(expenses.router)
