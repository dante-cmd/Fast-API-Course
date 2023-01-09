# ---------------------------------------
# ------------ Request Body-------------
# --------------------------------------

# A `request body` is data sent by the client to your API.
# A `response body` is the data your API sends to the client.

# To sent the data we must use POST operation. But FastAPI
# allow other opertions, PUT; DELETE, or PATH
# even GET (this is not usual)
from pydantic import BaseModel, Field
from fastapi import FastAPI, Body


names = [{"Lomo Saltado": 12.5}, {"Caldo de Gallina": 10.0}]

class Order(BaseModel):
    name: str
    description: str | None = None
    table: str

# If the default value of a field is `None`, that means, this fiel is optinal
app = FastAPI()

@app.post('/make_order')
async def make_order(order: Order):
    for name in names:
        if name.get(order.name):
            return name
    return "name not found"


# -------------------------------------------------------------------------------------

# Request with body + path + query parameters
# In @app.put() is the example
users_data = []
# more information about Field `https://fastapi.tiangolo.com/tutorial/body-fields/`

class User(BaseModel):
    user_id: int
    name: str = Field(default="Sony", max_length=120)
    age: int

@app.get('/users')
async def get_users():
    return users_data

# If we specify a `data model`, e.g User like `Body`, that is, User=Body(), That means
# The data or body that receive is json with fiels {"user_input" = {"user_id": "", "name": "", "age": ""} }
# 

@app.post('/users')
async def post_user(user_input: User=Body(embed=True)):
    users_data.append(user_input.dict())
    # print(user_input.dict())
    return ["Append a new user"]


class UserUpdate(BaseModel):
    user_id: int
    new_name: str | None = None
    new_age: int | None = None

# bernoulli_response can be `cancel` or `done`
iterator_data = iter(users_data)

# path parameter -> user_id
# query parameter -> user_id
# body request  -> user_update

@app.put('/users/{user_id}')
async def update_user(user_id: int,
                      bernoulli_response: str,
                      user_update: UserUpdate | None = None):
    if bernoulli_response == "done":
        for i, user in enumerate(iterator_data):
            if user.get("user_id") == user_id:
                # delete
                users_data.pop(i)
                # update
                user['name'] = user_update.new_name if user_update.new_name else user['name']
                user['age'] = user_update.new_age if user_update.new_age else user['age']
                users_data.append(user)
                return "There were some changes" 
    return "There were not changes "