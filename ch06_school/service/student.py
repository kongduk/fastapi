from typing import List

from ch06_school.error import StudentNotFoundException
from ch06_school.model.student import StudentResponse
from ch06_school.data import student as student_data

def find_all() -> List[StudentResponse]:
    return student_data.find_all()

def find_by_id(student_id: int ) -> StudentResponse:
    _student = student_data.find_by_id(student_id)
    if _student is None:
        raise StudentNotFoundException(student_id)
    return _student
