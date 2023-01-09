import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:5500",
]
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex = r"http://localhost\:5500.*" , 
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]

)
@app.get("/")
async def add_process_time_header(request: Request):
    return {"response":120}


@app.post("/")
async def post_data(request: Request):
    response = await request.json()
    print(response)
    return {"susu":120}