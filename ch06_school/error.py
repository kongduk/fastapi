# get one 예외처리를 알아보자
from starlette import status


class Missing(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

class Duplicate(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class SchoolException(Exception):
    def __init__(self, msg, status_code: int = status.HTTP_400_BAD_REQUEST):
        self.msg = msg
        self.status_code = status_code

class StudentNotFoundException(SchoolException):
    def __init__(self, student_id: int):
        super().__init__(
            msg=f"학생 id가 {student_id}인 학생을 찾을 수 없습니다 ~~!",
            status_code=status.HTTP_404_NOT_FOUND
        )