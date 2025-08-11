from fastapi import FastAPI
from src.api.contollers import web_scraper

app = FastAPI()

app.include_router(web_scraper.router, prefix="/web_scraper", tags=["web_scraper"])
