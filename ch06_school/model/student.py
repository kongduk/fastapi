from pydantic import BaseModel

from ch06_school.model.department import DepartmentName

class Student(BaseModel):
    name: str
    score: float

class StudentResponse(Student):
    id: int
    department: DepartmentName
