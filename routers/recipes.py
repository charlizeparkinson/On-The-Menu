from fastapi import APIRouter

router = APIRouter()

@router.post("/recipes/search")
def search_recipes():
    return {"message": "recipe endpoint is working!"}