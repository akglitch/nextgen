from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id:int
    title:str
    image:str
    description:str
    tags:List[str]
    location:str



    class Config: 
        schema_extra = {
            "example":{
                "title" :"fastApi Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description":"we will be discussing the contents of the fastApi book in this event.Ensure to come with your own copy to win gifts!",
                "tags":["python","fastapi","book","launch"],
                "location":"google meet"
            }
        }