from pydantic import BaseModel
from typing import Optional

class Department(BaseModel):
    name: str
    quota: int
    description: Optional[str] = None

class DepartmentResponse(Department):
    id: int

class DepartmentName(BaseModel):
    name: Optional[str]
