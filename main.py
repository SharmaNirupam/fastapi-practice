from typing import Optional

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Nirupam",
        "age": 24,
    },
    2: {
        "name": "John",
        "age": 25,
    },
    3: {
        "name": "Dave",
        "age": 24,
    }
}


class Student(BaseModel):
    name: str
    age: int



# api to get some data in the home route
@app.get("/")
def showdata():
    return {"hello": "hii"}


# api to get some data from an endpoint and path
@app.get("/student_details/{student_id}")
def student_details(student_id: int = Path(None, description="The id of the student to get", gt=0)):
    print(student_id)
    print('......................')
    print(students)
    print('......................')
    return students[student_id]


# api to get some data from an endpoint and query params
@app.get("/student_details_by_name")
# To make a query param optional : queryName :Optional[data type]=None
# Also when we try to put a required param after an optional parameter we get an error
# To overcome that we give a first parameter as '*' so that we can place optional and required parameters in any order
def get_student_by_name(*, student_name: Optional[str] = None, another_param: int):
    for student_id in students:
        if students[student_id]["name"] == student_name:
            return students[student_id]
    return {"data": "No such student exists"}


# Update the data ...Using pydantic for giving a schema like thing in the body
@app.post("/update_student")
def update_student_details(student_id:int, student: Student):
    print(".........data from user .........")
    print(student)
    print(".........data from user .........")
    if student_id in students:
        return {"message": "data already present"}
    students[student_id] = student
    print('......................')
    print(students)
    print('......................')
    return student
