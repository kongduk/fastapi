from . import con, cur
def save(filename: str,filepath: str):
    cur.execute(f"insert into images(filename,filepath) values('{filename},{filepath}')")
    con.commit()