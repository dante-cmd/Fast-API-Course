from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.responses import  RedirectResponse

app = FastAPI()
# ------ Making a redirection ----------


# @app.get("/redirect")
# async def redirect():
#     return RedirectResponse("https://www.youtube.com/watch?v=IgCfZkR8wME&t=1342s")

@app.get("/redirect")
async def redirect():
    return RedirectResponse("/new-url", status_code=status.HTTP_301_MOVED_PERMANENTLY)