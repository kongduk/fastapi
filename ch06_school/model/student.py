#학생 생성시 쓸 클래스
from pydantic import BaseModel

from ch06_school.model.department import Department


class Student(BaseModel):
    name : str
    score : float

class StudentResponse(Student):
    id: int
    department: Department