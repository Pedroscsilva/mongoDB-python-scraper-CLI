from tech_news.analyzer.reading_plan import (ReadingPlanService)  # noqa: F401, E261, E501
from unittest.mock import Mock

import pytest

all_news = [
    {
        "url": "https://blog.betrybe.com/carreira/oratoria/",
        "title": "Oratória: passo a passo para falar bem e se destacar!",
        "writer": "Lucas Custódio",
        "summary": "Sabemos que a arte de contar histórias surge de tempos imemoriais, com seres humanos carregando a habilidade de transmitir informações por meio da linguagem em sua essência. No entanto, o que podemos não saber é que a arte de usar a linguagem para construir discursos polidos e impactantes também não é de hoje. Tanto os diálogos do filósofo Platão quanto os discursos excepcionais de Cícero na Roma Antiga utilizavam uma técnica milenar para encantar audiências: a oratória.",
        "reading_time": 15,
        "timestamp": "08/07/2022",
        "category": "Carreira"
    },
    {
        "url": "https://blog.betrybe.com/noticias/orkut-voltou-o-que-se-sabe-ate-agora-sobre-o-retorno/",
        "title": "Orkut voltou: o que se sabe até agora sobre o retorno da rede",
        "writer": "Allan Camilo",
        "summary": "Em meados de abril deste ano, o domínio do Orkut foi reativado. O site, que para muitos brasileiros foi o primeiro contato com uma rede social, “retornou” 8 anos após ser desativado. Porém, seu sucessor espiritual ainda está para ser lançado. Entenda a seguir se o Orkut realmente voltou à ativa.",
        "reading_time": 4,
        "timestamp": "08/07/2022",
        "category": "Notícias"
    },
    {
        "url": "https://blog.betrybe.com/noticias/dungleon-como-jogar/",
        "title": "Dungleon: como jogar o game que mistura RPG e Wordle [2022]",
        "writer": "Allan Camilo",
        "summary": "Cópias e spin-offs de jogos populares não são novidade. Derivados dos aplicativos Temple Run e Flappy Bird já fazem parte da cultura pop. Com o boom repentino de Wordle, onde deve-se inserir letras e descobrir a palavra do dia, gêneros diferentes de jogos se misturaram à jogabilidade tradicional. É assim que surgiu Dungleon, game que mistura RPGs e Wordle. A seguir, saiba tudo sobre ele.",
        "reading_time": 3,
        "timestamp": "07/07/2022",
        "category": "Notícias"
    },
    {
        "url": "https://blog.betrybe.com/linguagem-de-programacao/linguagem-lua/",
        "title": "Linguagem Lua: o que é, quais os princípios e como usar?",
        "writer": "Lucas Marchiori",
        "summary": "As linguagens de programação existentes, como PHP, Java e C#, geralmente são desenvolvidas por pessoas estrangeiras. Contudo, a linguagem Lua é considerada brasileira, criada nos laboratórios de uma faculdade carioca e pensada principalmente para o desenvolvimento de jogos.",
        "reading_time": 12,
        "timestamp": "06/07/2022",
        "category": "Linguagem de Programação"
    },
    {
        "url": "https://blog.betrybe.com/carreira/livros-sobre-lideranca/",
        "title": "Os 20 livros sobre liderança para líderes de sucesso!",
        "writer": "Lucas Custódio",
        "summary": "Muitas pessoas desejam saber qual é o segredo para uma liderança de sucesso. O que poucas sabem é que não existe uma fórmula mágica que funcionará em todo cenário, em todo contexto, todas as vezes. No entanto, diversas pessoas líderes experientes e bem sucedidas já compartilharam suas experiências, contando o que funcionou e o que não foi tão efetivo, poupando um valioso tempo para quem está chegando agora. E onde elas estão? Em livros sobre liderança!",
        "reading_time": 10,
        "timestamp": "04/07/2022",
        "category": "Carreira"
    }
]

mock_success = {
    "readable": [
        {
            "unfilled_time": 3,
            "chosen_news": [
                (
                    "Orkut voltou: o que se sabe até agora sobre o retorno da rede",
                    4,
                ),
                (
                    "Dungleon: como jogar o game que mistura RPG e Wordle [2022]",
                    3,
                ),
            ],
        },
        {
            "unfilled_time": 0,
            "chosen_news": [
                (
                    "Os 20 livros sobre liderança para líderes de sucesso!",
                    10,
                )
            ],
        },
    ],
    "unreadable": [
        ("Oratória: passo a passo para falar bem e se destacar!", 15),
        ("Linguagem Lua: o que é, quais os princípios e como usar?", 12),
    ],
}


def test_reading_plan_group_news(mocker):
    with pytest.raises(ValueError, match="Valor 'available_time' deve ser maior que zero"):
        ReadingPlanService.group_news_for_available_time(0)
    ReadingPlanService._db_news_proxy = Mock(return_value=all_news)
    news = ReadingPlanService.group_news_for_available_time(10)
    assert news == mock_success
