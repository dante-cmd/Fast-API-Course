# -----------------------------------------------
#----------------dynamic drop dow ---------------
#------------------------------------------------


from typing import Optional
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

languages_framework = {"Python":['Django', 'Flask', 'FastAPI'],
    "Ruby":['Rails', 'Sinatra'],
    "JavaScript":['Express', 'Hapi']}


@app.get('/dropdown', response_class=HTMLResponse)
async def dropdown(request:Request, language:str=None):
    if language:
        context = {'request':request, 'frameworks':languages_framework[language] }
        return templates.TemplateResponse('framework_options.html', context=context)

    context = {'request':request}
    return templates.TemplateResponse('dropdown.html', context=context)


# @app.get('/search', response_class=HTMLResponse)
# async def search(request:Request):
#     context = {'request':request}
#     return templates.TemplateResponse('search.html', context=context)


