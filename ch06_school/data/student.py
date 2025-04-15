from typing import List

from ch06_school.data import cur
from ch06_school.model.department import Department
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
        department=Department(name=d_name)
    )


def find_all() -> List[StudentResponse]:
    query = "select s.id, s.name,s.score,d.name from student s left join department d on deepartment.id = student.department_id"
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]

def find_by_id(student_id: int ) -> StudentResponse:
    query = ("select s.id, s.name, s.score, d.name "
             "from student s, department d on d.id = s.department_id "
             f"where s.id = {student_id}")
    cur.execute(query)
    return row_to_model(cur.fetchone())