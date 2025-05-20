from typing import Optional

import pymysql
from pymysql import Connection
from pymysql.cursors import Cursor

con: Optional[Connection] = None
cur: Optional[Cursor] = None

def get_connection():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="q1w2e3",
        db="study",
        charset="utf8"
    )

con = get_connection()
cur = con.cursor()