from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from func import ping

app = FastAPI(default_response_class=JSONResponse)

class CategoryRequest(BaseModel):
    name: str

@app.get("/model")
async def get_models():
    '''
    '''
    return [1, 2, 3, 4, 5]

@app.get("/ping")
async def ping_pong(text: str):
    return ping(text=text)

@app.post("/category")
async def create_category(request: CategoryRequest):
    '''
    '''
    return {"message": f"Category '{request.name}' has been created"}

