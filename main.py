from fastapi import FastAPI
from api.v1 import feedback_controller

app = FastAPI()

app.include_router(feedback_controller.router, prefix="/api/v1/feedback")