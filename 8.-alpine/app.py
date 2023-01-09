from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), 'static')

template = Jinja2Templates('templates')

@app.get('/', )
def index(request:Request):
    context = {'request':request}
    return template.TemplateResponse('index.html', context)