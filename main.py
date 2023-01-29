from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def root():
    return "holaaa fastapi uhhh"

@app.get('/url')
async def url():
    return {"url":"http://google.com"}