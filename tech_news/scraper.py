import requests
import time
import re
from tech_news.database import create_news
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
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get().strip()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get().strip()
    writer = selector.css("a.url.fn.n::text").get().strip()
    raw_rt = selector.css("li.meta-reading-time::text").get().strip()
    reading_time = int(re.findall(r'\d+', raw_rt)[0])
    summary = "".join(
        selector.css(".entry-content > p:nth-of-type(1) *::text")
        .getall()
    ).strip()
    category = selector.css("span.label::text").get().strip()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    tech_news = []
    page_url = "https://blog.betrybe.com/"
    while len(tech_news) < amount:
        working_page = fetch(page_url)
        all_news_links = scrape_updates(working_page)
        for news in all_news_links:
            html_content = fetch(news)
            news_obj = scrape_news(html_content)
            tech_news.append(news_obj)
            if len(tech_news) >= amount:
                break
        next_page_url = scrape_next_page_link(working_page)
        if next_page_url:
            page_url = next_page_url
        else:
            break
    create_news(tech_news)
    return tech_news
