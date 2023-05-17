import sys
from tech_news import scraper
from tech_news.analyzer import search_engine
from tech_news.analyzer import ratings


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
        0: get_tech_news,
        1: search_by_title,
        2: search_by_date,
        3: search_by_category,
        4: top_5_categories,
        5: exit_menu,
    }

    input_options = {
        0: "Digite quantas notícias serão buscadas:",
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a categoria:",
        4: None,
        5: None,
    }

    try:
        handler = options.get(int(user_option))
        if input_options.get(int(user_option)):
            input_text = input_options.get(int(user_option))
            user_input = input(input_text)
            handler(user_input)
        else:
            handler()
    except (ValueError, TypeError):
        sys.stderr.write("Opção inválida\n")


def get_tech_news(input):
    scraper.get_tech_news(int(input))


def search_by_title(input):
    result = search_engine.search_by_title(input)
    print(result)


def search_by_date(input):
    result = search_engine.search_by_date(input)
    print(result)


def search_by_category(input):
    result = search_engine.search_by_category(input)
    print(result)


def top_5_categories():
    result = ratings.top_5_categories()
    print(result)


def exit_menu():
    print("Encerrando script\n")
