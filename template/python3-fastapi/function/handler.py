from pydantic import BaseModel


class RequestModel(BaseModel):
    data: dict


class ResponseModel(BaseModel):
    data: dict


def handle(body: RequestModel):
    return ResponseModel.parse_obj(body).dict()
