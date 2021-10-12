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
    try:
        data=request.form.to_dict()
        print(data)
        return obj.add_task_model(data,list_id,token_data["data"][0]["id"])
    except Exception as e:
        print(str(e))
        return make_response({"error":str(e)},500)

@app.route("/task/read_task/<list_id>")
@cross_origin()
@token_authenticator()
def read_task(list_id):
    try:
        print(token_data["data"][0]["id"])
        return obj.read_task_model(list_id)
        
    except Exception as e:
        print(str(e))
        return make_response({"error":str(e)},500)

@app.route("/task/delete_task/<task_id>")
def delete_task(task_id):
    return obj.delete_task_model(task_id)

@app.route("/task/update_task/<task_id>")
def update_task(task_id):
    return obj.update_task_model(task_id)


