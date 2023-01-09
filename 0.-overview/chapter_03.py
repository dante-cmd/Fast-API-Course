from fastapi import FastAPI

# Create the server
app = FastAPI(debug=True)

# -----------------------------------------------------------
# -----------------Headers and cookies -----------------------
# -----------------------------------------------------------
from fastapi import Header

# to get the header of a web page, that include the Header
@app.get("/user_agent")
async def get_header(user_agent: str = Header(...)):
    print(user_agent)
    return {"user_agent": user_agent}


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

# --------------------
# ----- COOKIES-------
# --------------------

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
from fastapi import HTTPException, Body

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
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
# it works with pip install aiofiles
from os import path

app = FastAPI()

@app.get("/{file}")
async def get_file(request:Request, file:str):
    root_directory = path.dirname(path.dirname(__file__))
    picture_path = "{}\static\img\{}.webp".format(root_directory, file)
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


