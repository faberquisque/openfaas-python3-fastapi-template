from fastapi import FastAPI
from function import handler

app = FastAPI(openapi_url='/', docs_url=None, redoc_url=None)


app.post('/', response_model=handler.ResponseModel)(handler.handle)
