from tech_news.analyzer.reading_plan import (ReadingPlanService)  # noqa: F401, E261, E501
from unittest.mock import Mock

import pytest

all_news = [
    {
        "title": "Oratória: passo a passo para falar bem e se destacar!",
        "writer": "Lucas Custódio",
        "reading_time": 15,
        "timestamp": "08/07/2022",
        "category": "Carreira"
    },
    {
        "title": "Orkut: o que se sabe até agora sobre o retorno da rede",
        "writer": "Allan Camilo",
        "reading_time": 4,
        "timestamp": "08/07/2022",
        "category": "Notícias"
    },
    {
        "title": "Dungleon: como jogar o game que mistura RPG e Wordle",
        "writer": "Allan Camilo",
        "reading_time": 3,
        "timestamp": "07/07/2022",
        "category": "Notícias"
    },
    {
        "title": "Linguagem Lua: o que é, quais os princípios e como usar?",
        "writer": "Lucas Marchiori",
        "reading_time": 12,
        "timestamp": "06/07/2022",
        "category": "Linguagem de Programação"
    },
    {
        "title": "Os 20 livros sobre liderança para líderes de sucesso!",
        "writer": "Lucas Custódio",
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
                    "Orkut: o que se sabe até agora sobre o retorno da rede",
                    4,
                ),
                (
                    "Dungleon: como jogar o game que mistura RPG e Wordle",
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
    with pytest.raises(ValueError,
                       match="Valor 'available_time' deve ser maior que zero"):
        ReadingPlanService.group_news_for_available_time(0)
    ReadingPlanService._db_news_proxy = Mock(return_value=all_news)
    news = ReadingPlanService.group_news_for_available_time(10)
    assert news == mock_success
