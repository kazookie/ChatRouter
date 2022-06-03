from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@router.get("/stt", response_class=HTMLResponse)
def read_stt(request: Request):
    return templates.TemplateResponse('stt.html', {"request": request})

@router.get("/chat", response_class=HTMLResponse)
def read_chat(request: Request):
    return templates.TemplateResponse('chat.html', {"request": request})

@router.get("/setting", response_class=HTMLResponse)
def read_chat(request: Request):
    return templates.TemplateResponse('setting.html', {"request": request})