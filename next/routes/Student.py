
from fastapi import APIRouter,HTTPException,status
from  ..models.StudentModel import Student



student_router = APIRouter()

@student_router.post("items/")
async def post(student : Student) -> dict:
    student.name.capitalize()
    return student