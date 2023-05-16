import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url,
                                timeout=3,
                                headers={"user-agent": "Fake user-agent"}
                                )
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    links = selector.css("a.cs-overlay-link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_link = selector.css("a.next::attr(href)").get()
    return next_link


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
