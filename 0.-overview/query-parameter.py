from typing import List
from urllib import response
from fastapi import FastAPI

app = FastAPI()
# --------------------------------------------
# --------- Query parameters ----------------
# --------------------------------------------
@app.get("/items")
async def get_user(id_product: int = 1001, year: int = 2020):
    return {"id_product": id_product, "year": year}

# When you declare other function parameters that are not part of the path parameters, 
# they are automatically interpreted as "query" parameters.

# The query is the set of key-value pairs that go after the ? in a URL, separated by & characters
# If don't pass, by default, the return will be {"page": 1, "size": 10}

# http://127.0.0.1:8000/users/news?page=1&size=10
# `?page=90&size=60` -> this is query

from fastapi import Query
from pathlib import Path

# with `Query` we can 
# > set the default value like Query(default=None)
# > restrinct the possible values that can take
#   - Query(regex = pattern,max_length = int, min_lenght = int)
#   - Query(default=None) 
#      **As it will use that None as the default value,**
#        and that way make the parameter not required.
#   - Query(default = value)
#      => default value is value that can be an str|int|float|None|True|False
#   - Query(default = ... , min_length=value)
#      => we says that the variable is required, and the min length is value
#   - Query(gt=0)
#      => we force that the variable be greater than `0`

@app.get("/users/{type_file}")
async def get_user(
    author:str|None = Query(default=None),
    type_file: str = Path(regex=r'csv|xlsx|txt'), 
    year: str = Query(regex=r'20(?:([01]\d|2[012]))')
    
    ):
    """This function only allow 3 types of files and the years 2000-2022
    e.g.`?type_file=txt&year=2020`
    both are `required`
    If we don't pass these args it will return error
    """
    return {"type_file": type_file, "year": year, "author":author}



import pandas as pd

product_prices = pd.Series(
    [1.2, 2.2, 2.5], 
    index= ['Pepsi', 'Coca-Cola', 'Inca-Kola'])


@app.get("/")
async def get_prices(
    product_item:list[str]|None=Query(
        default=None,
        title="Get the prices of the products",
        description="Get the prices from data series created in pandas",
        alias="product-item"
        ),
):
    
    if product_item:
        result = product_prices.loc[product_item].values.tolist()
        return result 
    
    return "No exists products"

# --------------------------
# ------ Enumerate & Form---------
# --------------------------

from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from enum import Enum

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class ModelName(str, Enum):
    red = "red"
    blues = "blue"
    green = "black"


# Enum is used with options
# The only requeriment is valur of the Enum in the class must be the same 
# of the value of the option in HTML
# So, if exist red as a option in HTML, this must be included in class Enum. Here no matter the name of teh variable. e.g. green="black". Obviously, is recommended the name of the variable beain similar to value, 
# like red = "red" 

@app.get('/models/')
async def get_model(request:Request) :
    return templates.TemplateResponse('index.html', context={'request':request}) 

@app.post('/models/', response_class=HTMLResponse)
async def models(request:Request,model:ModelName=Form(...)):
    context = {'request':request}
    print(model.value)
    return templates.TemplateResponse('index.html', context = context)


# Multiple Parameters

# ----------------------------------------
# ----------- The request body  ----------
# ---------------POST --------------------
# ----------------------------------------

from fastapi import Body

# The body is the part of the HTTP request that contains raw data, representing documents,
# files, or form submissions. In a REST API, it's usually encoded in JSON and used to create
# structured objects in a database
# So, in `http://127.0.0.1:8000/users` 
# If we specify `name: str=Body(), age:int=Body()`
# this allow to do us request in format `json`,  like {"name": "John", "age": 39}
# WE CAN GET THE SAME WHEN SPECIFY A MODEL. BUT THE ADAVENTAGE IS WHICH WE CAN ADD TO BODY MODEL A FIELD
# IF WE ESPEFICY `Body()` in the variable.
#     e.g. => {"name": "John", "age": 39}
# 
# If we specify `name: str, age:int`, we need to specify field by field
# e.g. => name:Dante and age:10


@app.post("/users")
async def create_user(name: str=Body(), age:int=Body()):
    print(name, age)
    return {"name": name, "age": age}
