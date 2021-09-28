from flask import Flask,request,make_response,jsonify
app = Flask('src')
import jwt,re,json
from functools import wraps

token_data = {}

def token_authenticator():
    # print("1")
    def inner_decorator(fun):
        # print("2")
        @wraps(fun)
        def inner(*args,**kwargs):
            # print("1212")
            try:
                # print("3")    
                authorization = request.headers.get("authorization")
                # print(authorization)
                if re.match("^Bearer *([^ ]+) *$",authorization,flags=0):
                    # print("7878")
                    token = authorization.split(" ")[1]
                    # print(token)
                    decoded = jwt.decode(token,"EncryptionKey",algorithms="HS256")
                    # print(decoded["data"])
                    token_data["data"] = decoded["data"]
                    # print(token_data["data"])
                    return fun(*args,**kwargs)
                else:
                    # print("555")
                    return make_response({"error":"Invalid Token"})
            except Exception as e:
                # print("4")
                return make_response({"error":str(e)})
        return inner
    return inner_decorator

from src.controllers import *