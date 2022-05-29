from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@router.get("/stt", response_class=HTMLResponse)
def read_stt(request: Request):
    return templates.TemplateResponse('stt.html', {"request": request})