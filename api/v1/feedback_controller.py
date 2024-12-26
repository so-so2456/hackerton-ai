from fastapi import APIRouter, HTTPException
from schemas.feedback_model import FeedbackRequestModel, FeedbackResponseModel
from services.feedback_service import FeedbackService

router = APIRouter()
feedback_service = FeedbackService()

@router.post("/", response_model=FeedbackResponseModel)
async def post_data(data: FeedbackRequestModel):
    return feedback_service.feedback(data)