from src import app
from flask import request,make_response
from src.models.users_model import users_model
from flask_cors import CORS, cross_origin
import jsonify

uobj = users_model()

@app.route("/login",methods=["post"])
# @cross_origin()
def login():
    data=request.form
    post_data=jsonify.data
    print(data)
    return uobj.login_model(post_data)

@app.route("/add_user",methods=["POST"])
# @cross_origin()
def add_user():
    data=request.form.to_dict()
    return uobj.add_user_model(data)

@app.route("/read_user")
# @cross_origin()
def read_user():
    return uobj.read_user_model()

@app.route("/read_single_user/<id>")
# @cross_origin()
def read_single_user(id):
    return uobj.read_single_user_model(id)

@app.route("/update_user",methods=["post"])
# @cross_origin()
def update_user():
    return uobj.update_user_model(request.form)

@app.route("/delete_user",methods=["post"])
# @cross_origin()
def delete_user():
    return uobj.delete_user_model(request.form)