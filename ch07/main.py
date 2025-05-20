from urllib.request import Request

import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse

from ch07.error import UploadException
from ch07.web import upload

app = FastAPI()
app.include_router(upload.router)

@app.exception_handler(UploadException)
def school_exception_handler(request: Request, exc: UploadException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.msg
        }
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
