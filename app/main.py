from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import main_pages, api

app = FastAPI()

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Шаблоны Jinja2
templates = Jinja2Templates(directory="app/templates")

# Подключение маршрутов
app.include_router(main_pages.router)
app.include_router(api.router)

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)