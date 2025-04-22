# 쿼리 담당
#1. 테이블 생성
import sqlite3
from typing import List
from ch06_school.data import cur, con
from ch06_school.error import Missing, Duplicate
from ch06_school.model.department import Department, DepartmentResponse

cur.executescript("""
    create table if not exists department (
    id integer primary key autoincrement,
    name text not null unique,
    quota integer not null default 0,
    description text
    );
    insert or ignore into department(name, quota) values('sw',32);
    insert or ignore into department(name, quota) values('embedded sw',32);
    
""")

def row_to_model(entity: tuple) -> DepartmentResponse:
    id, name, quota, description = entity
    return DepartmentResponse(
        id = id,
        name = name,
        quota = quota,
        description = description
    )

def find_all() -> List[DepartmentResponse]:
    query = "select * from department"
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]

def find_by_id(dept_id) -> DepartmentResponse:
    query = f'select * from department where id = {dept_id}'
    cur.execute(query)
    row = cur.fetchone()
    print(row)
    if row:
        return row_to_model(row)
    else :
        raise Missing(msg=f"{dept_id} is not found")

def create(department: Department):
    query = ("insert into department(name, quota, description) values(:name, :quota, :description)")

    try:
        cur.execute(query, department.model_dump())
        con.commit()
        return department
    except sqlite3.IntegrityError:
        raise Duplicate(msg=f"{department.name} is duplicate!")

def update(dept_id: int, department: Department):
    query = ("update department "
             "set name = :name, quota=:quota, description=:description "
             "where id = :id")
    dto = DepartmentResponse(
        id = dept_id,
        name = department.name,
        quota= department.quota,
        description= department.description
    )
    cur.execute(query,dto.model_dump())
    if cur.rowcount <= 0:
        raise Missing(msg=f"{dept_id} is not found")
    con.commit()


def delete(dept_id: int):
    query = "DELETE FROM department WHERE id = :id"
    params = {"id": dept_id}

    cur.execute(query, params)

    if cur.rowcount <= 0:
        raise Missing(msg=f"{dept_id} is not found")

    con.commit()