from uuid import uuid4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Text, Optional
from datetime import datetime

# Create the server
app = FastAPI(debug=True)

# post model
class User(BaseModel):
    id_: Optional[str]
    name: str
    age: Optional[int] = None
    email: Optional[str] = None
    address: str = None
    city: str = None
    created_at: datetime = datetime.now()


posts = []
@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def read_item():
    return posts

@app.get("/posts/{id_}")
def read_item(id_):
    for item in posts:
        if item['id_'] == id_:
            return item
    raise HTTPException(status_code=404, detail="Post not found")
    

@app.delete("/posts/{id_}")
def delete_item(id_):
    for i, item in enumerate(posts):
        if item['id_'] == id_:
            posts.pop(i)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Post not found")

@app.put("/posts/{id_}")
def update_item(id_, item: User):
    for i, it in enumerate(posts):
        if it['id_'] == id_:
            # print(item)
            posts[i]['name'] = item.name
            posts[i]['address'] = item.address
            posts[i]['city'] = item.city
            return "updated item"
    raise HTTPException(status_code=404, detail="Post not found")


@app.post("/post")
async def create_post(user: User):
    user.id_ = uuid4().hex
    posts.append(user.dict())
    return {"body": user.dict()}