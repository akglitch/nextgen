from fastapi import FastAPI
from  .routes.Student import student_router

import uvicorn

app = FastAPI()

# Register routes

app.include_router(student_router)
