from fastapi import FastAPI

# Create the server
app = FastAPI(debug=True)

# When we go to the http://127.0.0.1:8000/home
# the return will be {'Hello':'world'}
@app.get('/home')
async def hello_world():
    return {'Hello':'world'}

# ----------------------------------
# ----- Path parameters ------------
# ----------------------------------

@app.get("/users/{idx}")
async def get_user(idx: int):
   return {"idx": idx}
# Only permits int. This happen due to we specify the type of data. Type hint
# We can pas more parameters adding `/`

# --------------------------------------------
# --------- Path parameters ----------------
# --------------------------------------------

from fastapi import Path
app = FastAPI()
bought = ['1055-ADQW', '6270-QPLK', '5065-ALOP']
@app.get("/users/licence/{licence}")
async def get_user(licence: str = Path(regex=r'(\d{4}-[A-Z]{4})$')):
    if licence in bought:
        return 'Your licence is actived'
    else:
        return 'Your licence is not actived'

# Other options for Path apart of regex
# gt: Greater than
# ge: Greater than or equal to
# lt: Less than
# le: Less than or equal to

# --------------------------------------------
# --------- Query parameters ----------------
# --------------------------------------------
@app.get("/users/news")
async def get_user(page: int = 1, size: int = 10):
    return {"page": page, "size": size}

# You simply have to declare them as arguments of your path operation function. If they
# don't appear in the path pattern, as they do for path parameters, FastAPI automatically
# considers them to be query parameters.
# If don't pass, by default, the return will be {"page": 1, "size": 10}

# http://127.0.0.1:8000/users/news?page=1&size=10
# `?page=90&size=60` -> this is query

from fastapi import Query

# we force the page to be greater than 0 and the size to be less than or equal to 100

@app.get("/users/news")
async def get_user(
    type_file: str = Query(regex=r'csv|xlsx|txt'), 
    year: str = Query(regex=r'20(?:([01]\d|2[012]))')):
    """This function only allow 3 types of files and the years 2000-2022
    e.g.`?type_file=txt&year=2020`
    """

    return {"type_file": type_file, "year": year}

# ----------------------------------------
# ----------- The request body  ----------
# ---------------POST --------------------
# ----------------------------------------

from fastapi import Body

# The body is the part of the HTTP request that contains raw data, representing documents,
# files, or form submissions. In a REST API, it's usually encoded in JSON and used to create
# structured objects in a database
# So, in `http://127.0.0.1:8000/users` we can post {"name": "John", age: 39}

@app.post("/users")
async def create_user(name: str = Body(), age: int = Body()):
    print(name, age)
    return {"name": name, "age": age}


# ---------------------------------------------
# --- pydantic models for data validation------
# ---------------------------------------------
from fastapi import FastAPI
from pydantic import BaseModel

# define the schema of the data
# name: str, age int
# we can add Form(...), like `name:str = Form(..)` in the base model

class User(BaseModel):
    name: str 
    age: int 

app = FastAPI()

@app.post("/users")
async def create_user(user: User):
    print(user.name, user.age, user.dict())
    return user


# Multiple objects
# we can pass Company inside create_user function

class Company(BaseModel):
    name: str
    location: int

# -----------------------------------------------
# ---------- Form data and file uploads ---------
# -----------------------------------------------

from fastapi import Form, UploadFile, File

# post data from `Form`
@app.post("/users")
async def create_user(name: str = Form(), age: int =Form()):
    return {"name": name, "age": age}

# File uploads----
app = FastAPI()
@app.post("/files")
async def upload_file(file: UploadFile = File()):
    print(file.content_type)
    return {"file_size": file.filename, 'content':file.content_type}


# -----------------------------------------------------------
# -----------------Headers and cookies -----------------------
# -----------------------------------------------------------
from fastapi import Header

# to get the header of a web page, that include the Header
@app.get("/user_agent")
async def get_header(user_agent: str = Header(...)):
    print(user_agent)
    return {"user_agent": user_agent}

# -----------------------------------------
# -----------The request object-----------
# -----------------------------------------
from fastapi import FastAPI, Request


app = FastAPI()
@app.get("/requests")
async def get_request_object(request: Request):
    # This request only get some information of the server
    return {"path": request.url.path, 'host':request.client.host}

# -----------------------------------------------------------------
# -----------------Customizing the response -----------------------
# -----------------------------------------------------------------

from fastapi import FastAPI, status
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    page:int
    year:int

app = FastAPI()

# change the response status
@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    return post

# DELETE
# Dummy database
posts = {50: Post(title="Hello", nb_views=100)}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
   posts.pop(id, None)
   return None

# ----------------------------------------------
# ----------- The response model ---------------
# ----------------------------------------------

from fastapi import FastAPI
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    nb_views: int

app = FastAPI()

# Given the dummy database
posts = {1: Post(title="Hello", nb_views=100)}

@app.get("/posts/{id}")
async def get_post(id: int):
    return posts[id]

# If we want show only part that we post
class PublicPost(BaseModel):
    title: str

@app.get("/posts/{id}", response_model = PublicPost)
async def get_post(id: int):
    return posts[id]

# Setting headers
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def custom_header(response: Response):
    response.headers["Custom-Header"] = "Custom-Header-Value"
    return {"hello": "world"}

# cookies
# Cookies can also be particularly useful when you want to maintain the user's state within
# the browser between each of their visits

from fastapi import Response

@app.get("/")
async def custom_cookie(response: Response):
    response.set_cookie("cookie-name", "cookie-value", max_age=86_400)
    print(response.headers)
    return {"hello": "world"}
# Here, we simply set a cookie, named cookie-name, with the value of cookie-value.
# It'll be valid for 86'400 seconds before the browser removes it.


# Setting the status code dynamically
# Raising HTTP errors
from fastapi import HTTPException

@app.post("/password")
async def check_password(password: str = Body(), password_confirm: str = Body()):
    if password != password_confirm:
        raise HTTPException( status.HTTP_400_BAD_REQUEST, detail="Passwords don't match.")
    return {"message": "Passwords match."}

# -------------------------------------------------
# --------- Building a custom response ------------
# -------------------------------------------------

# * HTMLResponse: This can be used to return an HTML response.
# * PlainTextResponse: This can be used to return raw text.
# * RedirectResponse: This can be used to make a redirection.
# * StreamingResponse: This can be used to stream a flow of bytes.
# * FileResponse: This can be used to automatically build a proper file response
# given the path of a file on the local disk

# HTMLResponse and PlainTextResponse:

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse

app = FastAPI()
@app.get('/html', response_class=HTMLResponse)
async def get_html():
    return """ <html> 
    <head> 
    <title>Hello world!</title>
    </head>
    <body>
    <h1>Hello world!</h1>
    </body>
    </html>"""

@app.get("/text", response_class=PlainTextResponse)
async def text():
    return "Hello world!"

# ------ Making a redirection ----------
from fastapi.responses import  RedirectResponse

@app.get("/redirect")
async def redirect():
    return RedirectResponse("https://www.youtube.com/watch?v=IgCfZkR8wME&t=1342s")

@app.get("/redirect")
async def redirect():
    return RedirectResponse("/new-url", status_code=status.HTTP_301_MOVED_PERMANENTLY)

# ------------- Serving a file -------------
from fastapi.responses import FileResponse
# it works with pip install aiofiles
from os import path


@app.get("/cat")
async def get_cat():
    root_directory = path.dirname(path.dirname(__file__))
    picture_path = path.join(root_directory, "assets", "cat.jpg")
    return FileResponse(picture_path)

# ---------------- Custom responses -------------
# Finally, if you really have a case that's not covered by the provided classes, you always have
# the option to use the Response class to build exactly what you need. With this class, you
# can set everything, including the body content and the headers.

@app.get("/xml")
async def get_xml():
    content = """<?xml version="1.0" encoding="UTF-8"?>
    <Hello>World</Hello>"""
    return Response(content=content, media_type="application/xml")

# You can view the complete list of arguments in the Starlette documentation at https://
# www.starlette.io/responses/#response.

# -----------------------------------------------------------------
# -----Structuring a bigger project with multiple routers----------
# -----------------------------------------------------------------

# 1. models (dir where are the models)
# 2. routers (dir where are the routers)
# 3. app - db (files the first is the main application and the later is database )
# The __init__.py files are there to properly define our directories as Python packages
# if we see this file in a directory then this is working like a Python packages


