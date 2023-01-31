from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from typing import List
import data
from config import create_config_doc
from middlewares import valid_subs
import errors

app = FastAPI()
create_config_doc(app)
global_data = data.create_data()


# Paths
@app.get("/home", tags=["Hello World"], status_code=200)
def show_home():
    return HTMLResponse("<h1>Hello world</h1>")


@app.get("/reload", tags=["Reload"], status_code=202)
def reload_data():
    global global_data
    global_data = data.create_data()
    return JSONResponse(content={"message": "Data reloaded successfully", "students": global_data})


@app.get("/students", tags=["Students"], status_code=202, response_model=List)
async def get_data():
    # print(global_data)
    return JSONResponse(content={"data": global_data})


@app.get("/students/{id}", tags=["Students"], status_code=200)
async def get_data_by_id(id: str):
    student = list(
        filter(lambda stud: stud["id"] == id, global_data["results"]))
    return JSONResponse(content=student[0] if student else {})


@app.patch("/students/{id}", tags=["Students"], status_code=202)
async def change_data_from_user(id: str, subscription: str):
    student = list(
        filter(lambda stud: stud["id"] == id, global_data["results"]))
    if (len(student) >= 1):
        result_valid = valid_subs(subscription)
        print(result_valid)
        if (result_valid):
            student[0]["data"]["SUBSCRIPTION"] = subscription
            return JSONResponse(content={"message": "Updated successfully", "student": student[0]})
        else:
            return JSONResponse(content=errors.bad_request("Invalid subscription"))
    # student['subscription'] = subscription
    # return JSONResponse(content=student)
