from content_generator.src.note_converter import NoteConverter

_INPUT_TEST_MD_TEXT = """
---
title: Господня вся земля
original_title: This Is My Father's World
poet: Maltbie Davenport Babcock
translator: [[Даниил Александрович Ясько]]
composer: Franklin L. Sheppard
song_of_rebirth: 2507
published: 1901
---
#hymn

## История написания

Некоторая история.

## Интересные факты

Музыка была взята за основу в теме Шира в Властелине колец.

## Ссылки

- [Hymnary.org](https://hymnary.org/text/this_is_my_fathers_world_and_to_my)
- [Wikipedia](https://en.wikipedia.org/wiki/This_Is_My_Father%27s_World)

"""

_EXPECTED_MD_TEXT = """Title: Господня вся земля
Date: 1993-06-12
Categories: Гимны

Оригинальное название: This Is My Father's World

Поэт: Maltbie Davenport Babcock

Переводчик: Даниил Александрович Ясько

Композитор: Franklin L. Sheppard

Песнь возрождения: 2507

Дата написания: 1901




## История написания

Некоторая история.

## Интересные факты

Музыка была взята за основу в теме Шира в Властелине колец.

## Ссылки

- [Hymnary.org](https://hymnary.org/text/this_is_my_fathers_world_and_to_my)
- [Wikipedia](https://en.wikipedia.org/wiki/This_Is_My_Father%27s_World)

"""


def test_base_converting():
    converter = NoteConverter()
    print(converter.convert(_INPUT_TEST_MD_TEXT))
    assert converter.convert(_INPUT_TEST_MD_TEXT) == _EXPECTED_MD_TEXT
