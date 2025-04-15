from typing import Optional

from pydantic import BaseModel

from ch06_school.model.student import Student
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ch06_school.model.student import Student

class Department(BaseModel):
    name: str
    quota: int
    description: Optional[str] = None


#응답용 model
class DepartmentResponse(Department):
    id: int


class DepartmentName(BaseModel):
    name: str
class StudentResponse(Student):
    id: int
    department: DepartmentName

