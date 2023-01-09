from typing import List
from fastapi import FastAPI, Request, Form, UploadFile, File

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
             name_user: str = Form(alias='name-user'),
             cc_number: str = Form(alias='cc-number'),
             cc_month: str = Form(alias='cc-month'),
             cc_year: str = Form(alias='cc-year')):
    
    # alias come from the name of the `form` html.  
    
    # Save the sales
    
    # --- code ---
    # print data
    print(cc_number, name_user, cc_month, cc_year)
    context = {'request': request}
    
    return templates.TemplateResponse('index.html', context=context )


# File uploads----
@app.get("/upload/")
def get_files(request:Request):
    context = {'request':request}
    return templates.TemplateResponse('upload.html', context=context )


# VERSION ONLY FOR ONE FILE

# @app.post("/upload-file/")
# def upload_file(filename: UploadFile = File()):
#     # print(filename.file.read())
#     print(filename.filename)
#     metadata = {"file_size": filename.filename, 'content':filename.content_type}
#     print(metadata)
    
#     return "Successful"

@app.post("/upload-file-list/")
def upload_file(filename: List[UploadFile] = File()):
    for file in filename:
        print(file.filename)
        # read the files
        # print(file.file.read())
        metadata = {"file_size": file.filename, 'content':file.content_type}
        print(metadata)
    return "Successful"