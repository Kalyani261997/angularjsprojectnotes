from src import app,token_authenticator,token_data
from flask import request,make_response
from src.models.list_model import list_model
from flask_cors import CORS, cross_origin


obj=list_model()

@app.route("/add_task_list",methods=["post"])
@cross_origin()
@token_authenticator()
def add_task_list():
    data=request.form
    return obj.add_task_list_model(data,token_data["data"][0]["id"])

@app.route("/show_list")
@cross_origin()
@token_authenticator()
def show_list():
    return obj.show_list_model()

@app.route("/archieve_list")
@cross_origin()
@token_authenticator()
def archieve_list():
    return obj.archieve_list_model()

@app.route("/trash_list")
@cross_origin()
@token_authenticator()
def trash_list():
    return obj.trash_list_model()

@app.route("/read_list")
@cross_origin()
@token_authenticator()
def read_list():
    return obj.read_list_model()

@app.route("/delete_list/<id>")
def delete_list(id):
    return obj.delete_list_model(id)