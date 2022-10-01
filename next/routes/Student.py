
from fastapi import APIRouter,HTTPException,status
from  ..models.StudentModel import Student





student_router = APIRouter()

@student_router.post("/post_student", status_code=status.HTTP_201_CREATED)
async def post_message(student: Student):
    return student