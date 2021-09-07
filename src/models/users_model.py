from src import app
from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor
import jwt
import datetime


class users_model:
    def __init__(self):
        self.conn = psycopg2.connect(database ="to_do_list_app",user ="postgres",password ="123123",host ="localhost",port =5432)
        self.conn.set_session(autocommit=True)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def login_model(self, post_data):
        try:
            # print(post_data)
            self.cur.execute("select * from users where email='"+post_data["email"]+"' AND password='"+post_data["password"]+"' AND status='a'")
            rows = self.cur.fetchall()
            if len(rows) > 0:
                # print(rows)
                # rows = json.dumps(rows,indent=4,sort_keys=True,default=str)
                token = jwt.encode({"data":rows,"exp":datetime.datetime.utcnow()+datetime.timedelta(days=100)},"EncryptionKey")
                return make_response({"payload":token},200)
            else:
                return make_response({"error":"Please check the id or password"},403)
        except Exception as e:
            return make_response({"error":str(e)},500)

    def add_user_model(self,post_data):
        try:
            self.cur.execute("Insert into users(status,full_name,email,phone,password) values('a','"+post_data["full_name"]+"','"+post_data["email"]+"',"+post_data["phone"]+",'"+post_data["password"]+"')")
            return make_response({"success":"user created"},200)

        except Exception as e:
            print(str(e))
            return make_response({"error":str(e)},500)

    def read_user_model(self):
        try:
            self.cur.execute("select * from users")
            row=self.cur.fetchall()
            return make_response({"data":row},200)

        except Exception as e:
            return make_response({"error":str(e)},500)

    def read_single_user_model(self,id):
        try:
            self.cur.execute("select * from users where id="+id)
            row=self.cur.fetchall()
            return make_response({"data":row},200)

        except Exception as e:
            return make_response({"error":str(e)},500)

    def delete_user_model(self,id):
        try:
            self.cur.execute("delete from users where id="+id)
            row=self.cur.fetchall()
            return make_response({"data":row},200)

        except Exception as e:
            return make_response({"error":str(e)},500)
