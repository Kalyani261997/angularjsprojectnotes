from src import app
from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class task_model:
    def __init__(self):
        self.conn = psycopg2.connect(database ="to_do_list_app",user ="postgres",password ="123123",host ="localhost",port =5432)
        self.conn.set_session(autocommit=True)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def add_task_model(self,post_data,list_id,id):
        try:
            self.cur.execute("Insert into task(task,list_id,status,created_by) values('"+post_data["task"]+"',"+str(list_id)+",'a',"+str(id)+")")
            return make_response({"success":"task created"},200)

        except Exception as e:
            # print(str(e))
            return make_response({"error":str(e)},500)

    def read_task_model(self,list_id):
        try:
            self.cur.execute("select * from task where list_id="+list_id)
            select=self.cur.fetchall()
            print(select)
            return make_response({"data":select},200)

        except Exception as e:
            print(str(e))
            return make_response({"error":str(e)},500)

    def delete_task_model(self,task_id):
        try:
            self.cur.execute("DELETE from task where list_id="+task_id)
            return make_response({"success":"list_deleted"},200)

        except Exception as e:
            return make_response({"error":str(e)},500)

def update_task_model(self,task_id):
        try:
            self.cur.execute("UPDATE from task where list_id="+task_id)
            return make_response({"success":"list_deleted"},200)

        except Exception as e:
            return make_response({"error":str(e)},500)

