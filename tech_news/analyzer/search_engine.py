from tech_news.database import search_news


def search_by_title(title):
    pattern = f".*{title}.*"

    news = search_news({"title": {"$regex": pattern, "$options": "i"}})
    return [(d["title"], d["url"]) for d in news]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
