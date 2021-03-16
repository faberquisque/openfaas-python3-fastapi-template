from fastapi import FastAPI
from pydantic import BaseModel


# mandatory 'app' of class 'FastAPI'
app = FastAPI()


# Example Request Model
class Request(BaseModel):
    data: dict


# Example Response Model
class Response(BaseModel):
    data: dict


# Example root endpoint
@app.post('/', response_model=Response)
def default_get(body: Request):
    return Response.parse_obj(body).dict()
