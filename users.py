from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str

users_list=[User(id=1,name="maikol",surname="perdomo",url="maikol.dev",age=25),
            User(id=2,name= "huno", surname= "shan", url= "shan.dev",age=41),
            User(id=3,name="murk", surname="hansolo", url=21)]

@app.get("/usersjson")
async def usersjson():
    return [{"name":"maikol","surname":"perdomo","url":"maikol.dev","age":25},
    {"name":"huno","surname":"shan","url":"shan.dev","age":41},{"name":"murk","surname":"hansolo","url":"murk.dev","age":21}]

@app.get("/users")
async def users():
    return users_list

#Path search

@app.get("/user/{id}")
async def user(id:int):
    users= filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"no se ha encontrado el usuario"}

#Query search, look up something adding /?<example>=<value>

@app.get("/userquery")
async def userquery(id:int):
    return searchuser_id(id)

def searchuser_id(id:int):
    users= filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"no se ha encontrado el usuario"}
