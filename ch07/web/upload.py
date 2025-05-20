from fastapi import APIRouter, UploadFile, File
from starlette.responses import FileResponse

from ch07.serveice import upload as service

router = APIRouter(prefix="/uploads")

@router.post("")
def upload_file(file: UploadFile = File(...)):
    return service.save_image(file)

# @router.get("/image/{filename}")
# def get_image(filename: str):
#     file_path = service.get_image(filename)
#     return FileResponse(file_path ,media_type="image/jpeg")