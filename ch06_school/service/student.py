from typing import List

from ch06_school.model.student import StudentResponse
from ch06_school.data import student as student_data

def find_all() -> List[StudentResponse]:
    return student_data.find_all()

def find_by_id(student_id: int ) -> StudentResponse:
    return student_data.find_by_id(student_id)