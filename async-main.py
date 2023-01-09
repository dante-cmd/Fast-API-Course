from typing import AsyncGenerator
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("item.html", context=context)


class User(BaseModel):
    name:str = "Soul"
    age:int = 50

@app.post("/")
async def post_data(user:User):
    print(user.dict())
    return {"sas":"sasas"}
