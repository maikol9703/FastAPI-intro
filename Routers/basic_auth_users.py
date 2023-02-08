from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    fullname: str
    username: str
    email: str
    disabled: bool

user_db={
    "maikolp":{
        "fullname":"Maikol Perdomo",
        "username":"maikolp",
        "email":"maikolp@api.com",
        "disabled": False,
        "password":"1234"
    },
    "miguelh":{
        "fullname":"Miguel Hidalgo",
        "username":"miguelh",
        "email":"miguelp@api.com",
        "disabled": True,
        "password":"4321"
    }
     
}
