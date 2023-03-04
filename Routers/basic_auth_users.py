from fastapi import FastAPI,HTTPException,Depends,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestFormStrict,OAuth2AuthorizationCodeBearer

app=FastAPI()
oauth=OAuth2AuthorizationCodeBearer(tokenUrl="login")

class User(BaseModel):
    fullname: str
    username: str
    email: str
    disabled: bool

#inherits User class instances

class UserDB(User):
    password: str

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

def search_user(username:str):
    if username in user_db:
        return UserDB(user_db[username])

@app.post("/login")
async def login(form:OAuth2PasswordRequestFormStrict=Depends()):
    user_db=user_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400,detail="user not found")
    
    #user has a json structure from users_db
    user=search_user(form.username)
    if not form.password==user.password:
        raise HTTPException(status_code=400,detail=f"incorrect password for {form.username}")
    
    #if user exists it receives an access token whitch keeps the session open
    return {"access_token":user.username,"token_type":"bearer"}

#funtion to authenticate access token
#import status to get more info for status codes
async def current_me(token: str = Depends(oauth)):
    user= search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sorry, you don't have access to this info")

#retrieve data from the user
@app.get("user/me")
async def 
