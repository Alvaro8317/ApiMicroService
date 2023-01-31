from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from typing import List
import data
from config import create_config_doc
from middlewares import valid_subs
from errors import bad_request, exit_code, write_log
from students import Student

app = FastAPI()
create_config_doc(app)
student_data = data.create_data()


def invalid_id(bad_req: str, msg_code: str, code: int = 1):
    write_log(bad_req)
    exit_code(msg_code, code)


def select_a_student(id):
    return list(filter(lambda student: student["id"] == id, student_data["results"]))


def search_a_student(id):
    student = select_a_student(id)
    return (True if student else False)


# Paths
@app.get("/home", tags=["Hello EduNext"], status_code=200)
def show_home():
    return HTMLResponse("<h1>Hello EduNext</h1>")


@app.get("/reload", tags=["Reload"], status_code=202)
def reload_data():
    global student_data
    student_data = data.create_data()
    return JSONResponse(content={"message": "Data reloaded successfully", "students": student_data})


@app.get("/students", tags=["Students"], status_code=202, response_model=List)
async def get_data():
    return JSONResponse(content={"data": student_data})


@app.get("/students/{id}", tags=["Students"], status_code=200)
async def get_data_by_id(id: str):
    result = search_a_student(id)
    if (result):
        return JSONResponse(content=select_a_student(id))
    else:
        invalid_id("Invalid ID", "the ID does not exist or is badly formated")


@app.patch("/students/{id}", tags=["Students"], status_code=202)
async def change_student_subscription(id: str, subscription: str):
    try:
        result = search_a_student(id)
        if (result):
            selected_student = select_a_student(id)
            data = selected_student[0]["data"]
            levels = {"free": 1, "basic": 2, "premium": 3}
            student_instance = Student(data, levels)
            result_valid = valid_subs(subscription, levels)
            if (result_valid):
                student_instance.update_subscription(subscription)
                return JSONResponse(content={"message": "Updated successfully", "student": selected_student[0]})
            else:
                JSONResponse(content=bad_request("Invalid subscription"))
                exit_code("The target subscription level is not reachable",2)
        else:
            invalid_id("Invalid ID", "the ID does not exist or is badly formated")
    except Exception as err:
        write_log(err)
        exit_code("other unknown error", 3)
