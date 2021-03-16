from fastapi import FastAPI
from function import main

assert isintance(main.app, FastAPI)

app = main.app
