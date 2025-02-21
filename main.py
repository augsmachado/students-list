from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "year": 12
    }
}

class  Student(BaseModel):
    name: str
    age: int
    year: int

class  UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[int] = None

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

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"message": "Student already exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"message": "Student not found"}

    if student.name != None:
        students[student_id]["name"] = student.name

    if student.age != None:
        students[student_id]["age"] = student.age

    if student.year != None:
        students[student_id]["year"] = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"message": "Student not found"}

    del students[student_id]
    return {"message": "Student deleted successfully"}