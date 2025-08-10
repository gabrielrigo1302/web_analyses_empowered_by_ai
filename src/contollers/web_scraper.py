from fastapi import APIRouter

from src.services.web_scraper import WebScraperService

router = APIRouter()

@router.get("/")
def get_web_scraper():
    return WebScraperService.get_web_scraper()