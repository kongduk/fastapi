from fastapi import FastAPI
from web import department as department_web
from web import student as student_web
app = FastAPI()
app.include_router(department_web.router)

app.include_router(student_web.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", reload=True)