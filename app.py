from fastapi import FastAPI
from routers.ingredients import router as ingredients_router
from routers.recipes import router as recipes_router

app = FastAPI()

app.include_router(ingredients_router)
app.include_router(recipes_router)

"""
uvicorn app:app --reload
"""