from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["API"])

@router.get("/reviews")
async def get_reviews():
    # Динамические данные для блока "Отзывы"
    return [
        {"author": "Алексей Смирнов", "text": "КСТиУ — это место, где я нашел свое призвание!"},
        {"author": "Екатерина Орлова", "text": "Современный колледж с отличной атмосферой!"}
    ]

@router.get("/news")
async def get_news():
    # Динамические данные для блока "Новости"
    return [
        {"title": "Победа на конкурсе молодых инженеров", "url": "/news/1"},
        {"title": "День открытых дверей", "url": "/news/2"}
    ]