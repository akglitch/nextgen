from pydantic import BaseModel,EmailStr





class Student(BaseModel):
    name : str
    age : int
    email: EmailStr

    class Config:
        schema_extra ={
            "example":{
                "name":"kacey",
                "age":8,
                "email":"kayteezy@gmail.com" ,
            }
        }

