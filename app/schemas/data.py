from pydantic import BaseModel
class ScoreModel(BaseModel):
    name: str
    score: int