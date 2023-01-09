from typing import Optional
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/items', response_class=HTMLResponse)

async def main(request:Request, hx_trigger :Optional[str]=Header(None)):
    if hx_trigger == '1321':
        return "<h1>Title 1321</h1>"
    context = {'request':request}
    return templates.TemplateResponse('index.html', context=context)