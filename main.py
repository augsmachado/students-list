from typing import Optional
from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12"
    }
}



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

# Path parameters
@app.get("/get-student/{student_id}")
def get_student_by_id(student_id: int = Path(description="The ID student that you want to view", gt=0)):
    if student_id not in students:
        return {"message": "Student not found"}

    return students[student_id]

# Query parameters
@app.get("/get-by-name")
def get_student_by_name(*, name: Optional[str] = None):
    return next(
        (
            students[student_id]
            for student_id in students
            if students[student_id]["name"] == name
        ),
        {"message": "Student not found"},
    )