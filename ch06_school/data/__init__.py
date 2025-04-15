from sqlite3 import Connection, Cursor, connect
from typing import Optional

con: Optional[Connection] = None
cur: Optional[Cursor] = None

# 연결 담당
def get_db():
    global  con, cur
    #연결 여부 확인, 연결 안되어 있으면 연결하기
    if con is None:
        print("create")
        con = connect('./mydb.db',check_same_thread=False)
        cur = con.cursor()

get_db()