from fastapi import FastAPI
from routers.ingredients import router as ingredients_router

app = FastAPI()

app.include_router(ingredients_router)

"""
uvicorn app:app --reload
"""