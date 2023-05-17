from tech_news.database import find_news
from collections import Counter


def top_5_categories():
    news = find_news()
    categories = [item["category"] for item in news]
    category_count = Counter(categories)
    sorted_categories = sorted(category_count.keys(),
                               key=lambda x: (-category_count[x], x))
    return sorted_categories[:5]
