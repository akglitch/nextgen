
from fastapi import APIRouter,HTTPException,status
from  ..models.StudentModel import Student
from ..database import collection_name

from student_schema import students_serializer,student_serializer
from bson import ObjectId




student_router = APIRouter()


# post
@student_router.post("/", status_code=status.HTTP_201_CREATED)
async def post_student(student: Student):
    _id = collection_name.insert_one(dict(student))
    return students_serializer(collection_name.find({"_id":_id.inserted_id}))


# retrieve
@student_router.get("/")
async def get_students():
    students = students_serializer(collection_name.find())
    return students


@student_router.get("/{id}")
async def get_student(id:str):
    return students_serializer(collection_name.find_one({"_id": ObjectId(id)}))



#update
@student_router.put("/{id}")
async def update_student(id: str, student:Student):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(student)
    })
    return students_serializer(collection_name.find({"_id": ObjectId(id)}))


#delete
@student_router.delete("/{id}")
async def delete_student(id:str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}