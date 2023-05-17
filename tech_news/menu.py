import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer import search_engine
from tech_news.analyzer.ratings import top_5_categories


def analyzer_menu():
    main_menu = """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair."""

    user_option = input(main_menu)

    options = {
        0: get_tech_news_menu,
        1: search_by_title_menu,
        2: search_by_date_menu,
        3: search_by_category_menu,
        4: top_5_categories_menu,
        5: exit_menu,
    }

    try:
        handler = options.get(int(user_option))
        handler()
    except ValueError:
        sys.stderr.write("Opção inválida")


def get_tech_news_menu():
    amount = int(input("Digite quantas notícias serão buscadas:"))
    result = get_tech_news(amount)
    sys.stdout.write(result)


def search_by_title_menu():
    title = input("Digite o título:")
    result = search_engine.search_by_title(title)
    sys.stdout.write(result)


def search_by_date_menu():
    date = input("Digite a data no formato aaaa-mm-dd:")
    result = search_engine.search_by_date(date)
    sys.stdout.write(result)


def search_by_category_menu():
    category = input("Digite a categoria:")
    result = search_engine.search_by_category(category)
    sys.stdout.write(result)


def top_5_categories_menu():
    result = top_5_categories()
    sys.stdout.write(result)


def exit_menu():
    sys.stdout.write("Encerrando script")
