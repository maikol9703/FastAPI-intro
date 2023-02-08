#pip install "fastapi[all]"

from fastapi import FastAPI
from Routers import products
from Routers import users
from fastapi.staticfiles import StaticFiles

app=FastAPI()

#Router
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get('/')
async def root():
    return "holaaa fastapi uhhh"

@app.get('/url')
async def url():
    return {"url":"http://google.com"}