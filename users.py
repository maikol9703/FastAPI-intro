from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int

users_list=[User(id=1,name="maikol",surname="perdomo",url="maikol.dev",age=25),
            User(id=2,name= "huno", surname= "shan", url= "shan.dev",age=41),
            User(id=3,name="murk", surname="hansolo", url="murk.com",age=18)]

@app.get("/usersjson")
async def usersjson():
    return [{"name":"maikol","surname":"perdomo","url":"maikol.dev","age":25},
    {"name":"huno","surname":"shan","url":"shan.dev","age":41},{"name":"murk","surname":"hansolo","url":"murk.dev","age":21}]

@app.get("/users")
async def users():
    return users_list

#Path search, demands an id

@app.get("/user/{id}")
async def user(id:int):
    users= filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"user not found"}

#Query search, look up something adding /?<example>=<value>

@app.get("/userquery")
async def userquery(id:int):
    return searchuser_id(id)

#Post creates a new user if it doesn't exist

@app.post("/user/")
async def user(user:User):
    if type(searchuser_id(user.id))==User:
         return {"error":"user already registered"}
    else:
        users_list.append(user)
        return user

#Put updates an entire user or just some parts of it

@app.put("/user/")
async def user(user:User):
    found=False
    for index,saved_user in enumerate(users_list):
        if saved_user.id==user.id:
            users_list[index]=user
            found=True

    if found:
        return user
    else:
        return {"error":"User not found"}

#Delete, deletes an user if found

@app.delete("/user/{id}")
async def user(id:int):
    found=False
    for index,saved_user in enumerate(users_list):
        if saved_user.id==id:
            del users_list[index]
            found=True
            return "User deleted succesfully"

    if not found:
        return {"error":"user hasn't been deleted"}

def searchuser_id(id:int):
    users= filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"user not found"}
