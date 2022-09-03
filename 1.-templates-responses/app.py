from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    url_path_id = request.url_for('static', path='/img/{}.webp'.format(id))
    context = {"request": request, "id": id, "url_path_id": url_path_id}
    return templates.TemplateResponse("item.html", context=context)
