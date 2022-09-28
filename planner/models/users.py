from pydantic import BaseModel,EmailStr
from typing import Optional,List
from models.events import Event



class User(BaseModel):
    email: EmailStr
    password:str
    events:Optional[List[Event]]


    class Config:
        schema_extra ={
            "example":{
                "email":fastapi@packt.com,
                "username":"kaytee",
                "events":[],
            }
        }



class UserSignIn(BaseModel) :
    email:EmailStr
    password:str


    class Config:
        schema_extra = {
            "example" : {
                "email":fastapi@gmail.com,
                "password":"strong",
                "events":[],
            }
        }