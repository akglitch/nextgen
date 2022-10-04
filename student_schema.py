def student_serializer(student) -> dict:
    return{
        "id" :str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "email":student["email"]
    }


def students_serializer(students) ->list:
    return [student_serializer(student) for student in students]