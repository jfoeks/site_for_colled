from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

# Главная страница
@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# О колледже
@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# Программы
@router.get("/programs", response_class=HTMLResponse)
async def programs(request: Request):
    return templates.TemplateResponse("programs.html", {"request": request})

# Поступление
@router.get("/admission", response_class=HTMLResponse)
async def admission(request: Request):
    return templates.TemplateResponse("admission.html", {"request": request})

# Новости
@router.get("/news", response_class=HTMLResponse)
async def news(request: Request):
    return templates.TemplateResponse("news.html", {"request": request})

# Контакты
@router.get("/contacts", response_class=HTMLResponse)
async def contacts(request: Request):
    return templates.TemplateResponse("contacts.html", {"request": request})
