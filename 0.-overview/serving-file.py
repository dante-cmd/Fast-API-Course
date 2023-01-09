from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
# it works with pip install aiofiles
from os import path

app = FastAPI()

# @app.get('/')
# def index():
#     return "Hello"

@app.get("/{file}")
async def get_file(request:Request, file:str):
    print(file)
    root_directory = path.dirname(path.dirname(__file__))
    picture_path = "{}\static\img\{}.webp".format(root_directory, file)
    return FileResponse(picture_path)