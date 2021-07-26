from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel

class ApiInput(BaseModel):
    numbers: list



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/sum')
async def do_sum(data: ApiInput):
    print(data)
    return {}