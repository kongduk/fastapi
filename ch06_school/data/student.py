from typing import List

from fastapi import Body

from ch06_school.data import cur, con
from ch06_school.model.department import Department, DepartmentName
from ch06_school.model.student import StudentResponse


cur.executescript("""
    create table if not exists student (
    id integer primary key autoincrement,
    name text not null,
    score real default 0,
    department_id integer,
    foreign key (department_id) references department(id)
    );
    insert or ignore into student(name, score) values('choi',99.9);
    insert or ignore into student(name, score, department_id) values('jung',98.9, 1);

""")

def row_to_model(entity: tuple) -> StudentResponse:
    id, name, score, d_name = entity
    return StudentResponse(
        id=id,
        name=name,
        score=score,
        department=DepartmentName(name=d_name)
    )


def find_all() -> List[StudentResponse]:
    query = "select s.id, s.name,s.score,d.name from student s left join department d on d.id = s.department_id"
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]

def find_by_id(student_id: int ) -> StudentResponse or None:
    query = ("select s.id, s.name, s.score, d.name "
             "from student s left join department d on d.id = s.department_id "
             f"where s.id = {student_id}")
    cur.execute(query)
    _student = cur.fetchone()
    print(_student)
    if _student is None:
        return None
    return row_to_model(_student)


def assignment_dept(student_id: int, department_id: int):
    # 학과 할당 쿼리
    update_query = "UPDATE student SET department_id = ? WHERE id = ?"
    cur.execute(update_query, (department_id, student_id))
    con.commit()
    # 변경된 학생 정보 조회
    select_query = "SELECT s.id, s.name, s.score, d.name FROM student s LEFT JOIN department d ON d.id = s.department_id WHERE s.id = ?"
    cur.execute(select_query, (student_id,))
    _student = cur.fetchone()


    if _student is None:
        return None
    return row_to_model(_student)

def find_by_dept_id_score_desc(department_id: int) -> List[StudentResponse]:
    query = """
        SELECT s.id, s.name, s.score, d.name
        FROM student s
        LEFT JOIN department d ON d.id = s.department_id
        WHERE s.department_id = ?
        ORDER BY s.score DESC;
    """
    cur.execute(query, (department_id,))
    return [row_to_model(row) for row in cur.fetchall()]
