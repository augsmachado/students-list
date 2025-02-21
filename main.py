from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def status():
    return {
        "name": "FastAPI Study",
        "version": "0.1.0"
    }

@app.get("/")
def index():
    return {
        "name": "First Data"
    }