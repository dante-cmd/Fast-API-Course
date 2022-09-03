from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Create the server
app = FastAPI(debug=True)

# Add the directory where the files templates are
# HTML files
templates = Jinja2Templates(directory='templates')

# mount a route where is the static files
# CSS, JavaScript and images if exists
app.mount('/static', StaticFiles(directory='static'), name='static')

# Create a route 
@app.get("/payment", response_class=HTMLResponse)
def get_form(request: Request):
    rangex = [ 40, 50, 60 ]
    context = {'request': request, 'rangex':rangex}
    return templates.TemplateResponse('index.html', context=context)

# https://freefrontend.com/css-forms/
@app.post("/payment", response_class=HTMLResponse)
def get_form(request: Request,
             name_user: str = Form(...),
             cc_number: str = Form(...),
             cc_month: str = Form(...),
             cc_year: str = Form(...)):
    # Save the sales
    # --- code ---
    # print data
    print(cc_number, name_user, cc_month, cc_year)
    context = {'request': request}
    
    return templates.TemplateResponse('index.html', context=context )