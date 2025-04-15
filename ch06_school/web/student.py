from typing import List

from fastapi import APIRouter, Path

from ch06_school.model.student import StudentResponse
from ch06_school.service import student as service

router = APIRouter(prefix="/students")

@router.get("")
def get_all() -> List[StudentResponse]:
    return  service.find_all()

@router.get("/{student_id}")
def get_by_id(student_id: int = Path()) -> StudentResponse:
    return service.find_by_id(student_id)
