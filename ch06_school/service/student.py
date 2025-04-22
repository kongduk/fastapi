from typing import List

from ch06_school import service
from ch06_school.error import StudentNotFoundException, AssignDepartmentException
from ch06_school.model.department import Department
from ch06_school.model.student import StudentResponse, Student, AssignDepartment
from ch06_school.data import student as student_data
from ch06_school.data import department as department_data


def find_all() -> List[StudentResponse]:
    return student_data.find_all()


def find_by_id(student_id: int) -> StudentResponse:
    _student = student_data.find_by_id(student_id)
    if _student is None:
        raise StudentNotFoundException(student_id)
    return _student

def assign_department(student_id:int, department_id:int, assign_dto: AssignDepartment) -> StudentResponse or None:
    assign_ok = student_data.assignment_dept(student_id, department_id)
    print(assign_ok)
    _students = student_data.find_by_dept_id_score_desc(assign_dto.department_id)
    print(_students)
    _department = department_data.find_by_id(assign_dto.department_id)
    print(_department)
    if len(_students) > _department.quota:
        sorry_student = student_data.update(AssignDepartment(student_id=_students[-1].id, department_id=None))
        raise AssignDepartmentException(sorry_student.name)
    return assign_ok

