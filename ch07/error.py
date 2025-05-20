# get one 예외처리를 알아보자
from starlette import status

class UploadException(Exception):
    def __init__(self, msg, status_code: int = status.HTTP_400_BAD_REQUEST):
        self.msg = msg
        self.status_code = status_code

class InvalidImageFormatException(UploadException):
    def __init__(self):
        super().__init__(
            msg="only image uploads allowed"
        )

class ImageNotFoundException(UploadException):
    def __init__(self):
        super().__init__(
            msg=f"image not found",
            status_code=status.HTTP_404_NOT_FOUND
        )