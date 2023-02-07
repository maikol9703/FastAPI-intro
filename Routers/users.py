from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

router=APIRouter(prefix="/user",tags=["user"],responses={404:{"message":"page not found"}})

class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int

users_list=[User(id=1,name="maikol",surname="perdomo",url="maikol.dev",age=25),
            User(id=2,name= "huno", surname= "shan", url= "shan.dev",age=41),
            User(id=3,name="murk", surname="hansolo", url="murk.com",age=18)]

@router.get("/usersjson")
async def usersjson():
    return [{"name":"maikol","surname":"perdomo","url":"maikol.dev","age":25},
    {"name":"huno","surname":"shan","url":"shan.dev","age":41},{"name":"murk","surname":"hansolo","url":"murk.dev","age":21}]

@router.get("/users")
async def users():
    return users_list

#Path search, demands an id

@router.get("/{id}",status_code=201)
async def user(id:int):
    users= filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=400, detail="user not found")

#Query search, look up something adding /?<example>=<value>

@router.get("/userquery",status_code=201)
async def userquery(id:int):
    return searchuser_id(id)
    

#Post, creates a new user if it doesn't exist

@router.post("/",status_code=201)
async def user(user:User):
    if type(searchuser_id(user.id))==User:
         raise  HTTPException(status_code=404, detail="user already registered")
    else:
        users_list.append(user)
        return user

#Put, updates an entire user or just some parts of it

@router.put("/",status_code=201)
async def user(user:User):
    found=False
    for index,saved_user in enumerate(users_list):
        if saved_user.id==user.id:
            users_list[index]=user
            found=True

    if found:
        return user
    else:
        raise HTTPException(status_code=400,detail="User not updated")

#Delete, deletes an user if found

@router.delete("/{id}",status_code=201)
async def user(id:int):
    found=False
    for index,saved_user in enumerate(users_list):
        if saved_user.id==id:
            del users_list[index]
            found=True
            return "User deleted succesfully"

    if not found:
        raise HTTPException(status_code=404,detail="user hasn't been deleted")

def searchuser_id(id:int):
    users= filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=400,detail="user not found")
