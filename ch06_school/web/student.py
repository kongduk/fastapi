from typing import List

from exceptiongroup import catch
from fastapi import APIRouter, Path, HTTPException, Body
from starlette import status

from ch06_school.error import StudentNotFoundException
from ch06_school.model.department import Department
from ch06_school.model.student import StudentResponse, Student, AssignDepartment
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

@router.post("")
def create(student: Student) -> StudentResponse:
    return service.create(student)

@router.patch("/{student_id}")
def assignment(student_id: int = Path(...), assign_dto: AssignDepartment = Body(...)):
    return service.assign_department(student_id, assign_dto.department_id, assign_dto)  # assign_dto를 전체로 전달

