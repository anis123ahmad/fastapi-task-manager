
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI Task Manager",
        "status": "Application is running"
    }


@app.get("/about")
def about():
    return {
        "project": "FastAPI Task Manager",
        "version": "1.0"
    }
