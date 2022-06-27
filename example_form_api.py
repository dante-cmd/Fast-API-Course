from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# from frontend.style import front


# Create the server
app = FastAPI(debug=True)

# Add the directory where the files templates are
templates = Jinja2Templates(directory='frontend/pages')

# mount a route where is the static files
app.mount('/frontend/style', StaticFiles(directory='frontend/style'), name='style')

@app.get("/users" , response_class=HTMLResponse)
def get_form(request:Request):

    return templates.TemplateResponse('index.html', {'request':request})

@app.post("/users", response_class=HTMLResponse)
def get_form(request:Request,username :str =Form(...), password:str=Form(...)):
    print(username, password)

    return templates.TemplateResponse('index.html', {'request':request})


# uvicorn to_try:app --reload