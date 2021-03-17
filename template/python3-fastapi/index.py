from fastapi import FastAPI
from function import main

assert isinstance(main.app, FastAPI)

app = main.app
