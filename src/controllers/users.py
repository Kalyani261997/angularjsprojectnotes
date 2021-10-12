from src import app, token_authenticator,token_data
from flask import request,make_response
from src.models.users_model import users_model
from flask_cors import CORS, cross_origin
import jwt

uobj = users_model()

@app.route("/login",methods=["POST"])
@cross_origin()
def login():
    data=request.form.to_dict()
    # post_data=jwt.data
    # print(data)
    return uobj.login_model(data)

@app.route("/add_user",methods=["POST"])
@cross_origin()
def add_user():
    data=request.form.to_dict()
    return uobj.add_user_model(data)

@app.route("/read_user")
@cross_origin()
@token_authenticator()
def read_user():
    return uobj.read_user_model()

@app.route("/read_single_user/<id>")
@cross_origin()
def read_single_user(id):
    return uobj.read_single_user_model(id)

@app.route("/update_user",methods=["post"])
@cross_origin()
@token_authenticator()
def update_user():
    return uobj.update_user_model(request.form,token_data["data"][0]["id"])

@app.route("/delete_user",methods=["post"])
@cross_origin()
def delete_user():
    return uobj.delete_user_model(request.form)