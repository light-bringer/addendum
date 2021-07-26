import time
import os
from typing import List, Optional
from fastapi import FastAPI, Request, Response, status
from pydantic import BaseModel, validator
from adder_api import Log

from adder_api.exceptions import IncorrectInputLengthException, IncorrectInputTypeException
from adder_api.adder import array_sum, validate




app = FastAPI()
worker = os.getpid()

class ApiInputModel(BaseModel):
    numbers: list
    # numbers: List[int]


class ApiOutputModel(BaseModel):
    response: Optional[int] = None
    error   : Optional[str] = None
    status  : int


@app.on_event("startup")
async def startup_event():
    Log.debug("API Server Startup! worker : {}".format(worker))


@app.on_event("shutdown")
def shutdown():
    print('shutdown')
    Log.debug("API Server Shutdown! worker : {}".format(worker))


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
async def root():
    Log.debug('Hello World!')
    return {"message": "Hello World"}


@app.post('/sum', status_code=status.HTTP_200_OK, response_model=ApiOutputModel)
async def do_sum(data: ApiInputModel, response: Response):
    Log.debug("Inside Sum API")
    return_dict = {}
    try:
        array = validate(array=data.numbers, json=True)
        Log.info("validated array: {}".format(array))
        total_sum = array_sum(array=array)
        Log.info("Total Sum : {}".format(total_sum))
        return_dict = {
            "status": status.HTTP_200_OK,
            "response": total_sum
        }
    except IncorrectInputTypeException:
        Log.warning("Inputs are not numeric!")
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return_dict = {
            "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "error": "All inputs must be numeric"
        }

    except IncorrectInputLengthException:
        Log.warning("Inputs length is not equal to 3!")
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return_dict = {
            "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "error": "Exactly 3 numbers are required"
        }

    Log.info("Exiting Sum API")
    return return_dict