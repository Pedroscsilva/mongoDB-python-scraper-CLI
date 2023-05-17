# MongoDB Python Scraper CLI

This is a scraper that extracts news from a blog and save them in a mongo database for further analysis.

After cloning the project, execute the following commands in your terminal at the root of the project to make it work:

1 - Create and access the python virtual environment

`python3 -m venv .venv && source .venv/bin/activate`

2 - Install the packages

`python3 -m pip install -r dev-requirements.txt`

3 - Run the docker container to up a mongo database. (The default port is 27017, so if you are already using it you will need to change the docker-compose.yml and tech_news/database.py in order to up the container).

`docker-compose up -d mongodb`

4 - Enter the CLI

`tech-news-analyzer`

You should be prompted with the following screen:

```bash
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
```

The CLI is in portuguese, but it translates to:

```bash
Select one of the following options:
 0 - Populate the database with news;
 1 - Search news by title;
 2 - Search news by date;
 3 - Search news by category;
 4 - List top 5 categories;
 5 - Exit.
```
