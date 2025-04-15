# db 연결
from sqlite3 import Connection, connect, Cursor
from typing import Optional

conn: Optional[Connection] = None
cur: Optional[Cursor] = None


def get_db() -> Optional[Connection]:
    global conn, cur
    if conn is None:
        print("connection")
        conn = connect("mydb.db")
        cur = conn.cursor()

get_db()