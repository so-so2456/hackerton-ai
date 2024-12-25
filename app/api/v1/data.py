from fastapi import APIRouter, HTTPException
from schemas.data import ScoreModel
from services.data_service import DataService

router = APIRouter()
data_service = DataService()

@router.get("/", response_model=ScoreModel)
async def get_data():
    return data_service.get_data()

@router.post("/", response_model=ScoreModel)
async def post_data(data: ScoreModel):
    return data_service.post_data(data)