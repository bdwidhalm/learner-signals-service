from fastapi import FastAPI
from .routers import signals

app = FastAPI()

app.include_router(signals.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

