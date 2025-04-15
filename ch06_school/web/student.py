from typing import List

from fastapi import APIRouter, Path, HTTPException
from starlette import status

from ch06_school.error import StudentNotFoundException
from ch06_school.model.student import StudentResponse
from ch06_school.service import student as service

router = APIRouter(prefix="/students")

@router.get("")
def get_all() -> List[StudentResponse]:
    return  service.find_all()

@router.get("/{student_id}")
def get_by_id(student_id: int = Path()) -> StudentResponse:
    # try:
    #     return service.find_by_id(student_id)
    # except StudentNotFoundException as e:
    #     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
    #                         detail=e.msg)
    return service.find_by_id(student_id)
