import datetime
from tech_news.database import search_news


def search_by_title(title):
    pattern = f".*{title}.*"

    news = search_news({"title": {"$regex": pattern, "$options": "i"}})
    return [(d["title"], d["url"]) for d in news]


def check_date_format(date):
    try:
        datetime.date.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")


def search_by_date(date):
    check_date_format(date)
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
    formatted_date_str = date_obj.strftime("%d/%m/%Y")
    news = search_news({"timestamp": {"$eq": formatted_date_str}})
    return [(d["title"], d["url"]) for d in news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
