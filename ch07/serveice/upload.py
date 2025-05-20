import os
import shutil
from datetime import datetime

from fastapi import UploadFile, File

from ch07.data import upload as data
from ch07.error import InvalidImageFormatException

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_image(img:UploadFile = File(...)):
    if not img.content_type.startswith("image/"):
        raise InvalidImageFormatException()

    name, ext = os.path.splitext(img.filename)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    print(ext)
    save_filename = f"{name}_{timestamp}{ext}"

    filepath = os.path.join(UPLOAD_DIR, save_filename)
    with open(filepath, "wb") as fs:
        shutil.copyfileobj(img.file, fs)

    data.save(save_filename, filepath)
    return {
        "filename": save_filename,
        "filepath": filepath
    }