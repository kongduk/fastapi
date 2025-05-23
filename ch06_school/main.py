from fastapi import FastAPI, Request
from starlette import status
from starlette.responses import JSONResponse

from ch06_school.error import StudentNotFoundException, SchoolException, AssignDepartmentException, Missing
from web import department as department_web
from web import student as student_web

app = FastAPI()
app.include_router(department_web.router)
app.include_router(student_web.router)

@app.exception_handler(Missing)
def school_missing_handler(request: Request, exc: SchoolException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": exc.msg})
@app.exception_handler(SchoolException)
def school_exception_handler(request: Request, exc: SchoolException):
    return JSONResponse(status_code=exc.status_code, content={"success": False, "message": exc.msg})
@app.exception_handler(AssignDepartmentException)
def assign_department_exception_handler(request: Request, exc: AssignDepartmentException):
    return JSONResponse(status_code=exc.status_code, content={"success": False, "message": exc.msg})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
