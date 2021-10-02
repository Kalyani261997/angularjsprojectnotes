from src import app, token_authenticator,token_data
from flask import request,make_response
from src.models.task_model import task_model
from flask_cors import CORS, cross_origin
import jwt

obj=task_model()

@app.route("/task/add_task/<list_id>",methods=["POST"])
@cross_origin()
@token_authenticator()
def add_task(list_id):
    data=request.form
    return obj.add_task_model(data,list_id,token_data["data"][0]["id"])

@app.route("/task/read_task")
@cross_origin()
@token_authenticator()
def read_task():
    print(token_data["data"][0]["id"])
    return obj.read_task_model()

@app.route("/task/delete_task/<task_id>")
def delete_task(task_id):
    return obj.delete_task_model(task_id)

@app.route("/task/update_task")
def update_task():
    return obj.update_task_model()


