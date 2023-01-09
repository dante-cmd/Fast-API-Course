from fastapi import FastAPI, status, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

class User(BaseModel):
    name:str
    password:str
    email:str

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), 'static')

template = Jinja2Templates('templates')

@app.get('/', status_code=status.HTTP_200_OK)
def index(request:Request):
    navs = ['Home', 'Products', 'About Us']
    context = {'request':request,'navs':navs}
    return template.TemplateResponse('index.html', context)

@app.post('/', status_code=status.HTTP_201_CREATED)
def create_user(user:User):
    return 'User successfully created'
    