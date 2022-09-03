from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def get_request_object(request: Request):
    # This request only get some information of the server
    # get the URL
    print(request.url)
    # If we `mount static directory` we can obtain the 
    #  the url for some files 
    print(request.url_for('static', path = '/img/ab47d082-1786-4411-ad89-cb621da4c189.webp'))
    # get the host of the client
    print(request.client.host)
    return {"path": request.url.path, 'host':request.client.host}