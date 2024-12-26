from openai import OpenAI
from schemas.feedback_model import FeedbackRequestModel

class FeedbackService:
    def __init__(self):
        self.client = OpenAI()

    def feedback(self, data: FeedbackRequestModel):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are a helpful code assistant and only reply in Korean. {data.assignment_name}\n\n{data.context if data.context is not None else ''}"},
                {
                    "role": "user",
                    "content": f"{data.contents}\n\n{data.code}"
                }
            ]
        )
        return {"feedback": completion.choices[0].message.content}