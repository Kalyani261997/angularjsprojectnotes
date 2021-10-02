from src import app
from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class list_model:
    def __init__(self):
        self.conn = psycopg2.connect(database ="to_do_list_app",user ="postgres",password ="123123",host ="localhost",port =5432)
        self.conn.set_session(autocommit=True)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def add_task_list_model(self,post_data,id):
        try:
            self.cur.execute("INSERT INTO list(title,status,created_by)values('"+post_data["title"]+"','s',"+str(id)+")") 
            return make_response({"success":"list_created"},200)

        except Exception as e:
            return make_response({"error":str(e)},500)

    def show_list_model(self):
        try:
            self.cur.execute("SELECT * from list where status='s'") 
            select = self.cur.fetchall()
            return make_response({"data":select},200)

        except Exception as e:
            return make_response({"error":str(e)},500)

    def archieve_list_model(self):
        try:
            self.cur.execute("SELECT * from list where status='a'")
            select = self.cur.fetchall()
            return make_response({"data":select},200)

        except Exception as e:
            return make_response({"error":str(e)},500)

    def trash_list_model(self):
        try:
            self.cur.execute("SELECT * from list where status='t'")
            select = self.cur.fetchall()
            return make_response({"data":select},200)

        except Exception as e:
            return make_response({"error":str(e)},500)

    def read_list_model(self):
        try:
            self.cur.execute("select * from list")
            select = self.cur.fetchall()
            print(select)
            return make_response({"data":select},200)

        except Exception as e:
            return make_response({"error":str(e)},500)

    def delete_list_model(self,id):
        try:
            self.cur.execute("DELETE from list where id="+id)
            return make_response({"success":"list_deleted"},200)

        except Exception as e:
            return make_response({"error":str(e)},500)