from pydantic import BaseModel,EmailStr





class Student(BaseModel):
    id : int
    name : str
    task : str
    descriptioin: str

    class Config:
        schema_extra ={
            "example":{
              "id":1,
                "name":"kacey",
                "task": "singing",
                "description":"i usally sing jazz" ,
            }
        }


