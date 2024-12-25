from fastapi import FastAPI
from fastapi.responses import FileResponse
from api.v1 import data

app = FastAPI()

@app.get("/")
def index():
    return FileResponse('templates/index.html')

app.include_router(data.router, prefix="/api/v1/data")