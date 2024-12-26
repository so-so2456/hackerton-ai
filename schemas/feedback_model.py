from pydantic import BaseModel
class FeedbackRequestModel(BaseModel):
    assignment_name: str
    context: str
    code: str
    contents: str

class FeedbackResponseModel(BaseModel):
    feedback: str