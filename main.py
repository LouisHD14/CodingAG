import fastapi
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = fastapi.FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}", response_class=HTMLResponse)
def read_item(item_id: int, request: Request):
    if item_id == 69:
        return templates.TemplateResponse('item.html', {'request': request, 'item_id': item_id})
    return templates.TemplateResponse('404.html', {'request': request})
    