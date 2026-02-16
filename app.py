from fastapi import FastAPI
from routers.ingredients import router

app = FastAPI()

app.include_router(router)

"""
uvicorn app:app --reload
"""