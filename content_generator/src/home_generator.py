from jinja2 import Template

_TEMPLATE = """Title: О проекте
URL:
save_as: index.html

На сайте собраны заметки, истории и интересные факты для {{HYMN_NUM}}-ти песен.

Сайт будет полезен при подготовке к ведению собраний, для разъяснения церкви текстов, которые поются каждое воскресение для осмысленного разъяснительного пения.

Дополнительные источники:

- [Hymnary.org](https://hymnary.org/)
- [hymnal.net](https://www.hymnal.net/en/home)
- Джон Джулиан. Словарь гимнологии

# Контакты

Рахмаев Александр г. Йошкар-Ола ц. Благодать ([@rakhmaevao](https://t.me/rakhmaevao)).
"""


def generate_home(hymn_num: int) -> str:
    template = Template(_TEMPLATE)
    return template.render(HYMN_NUM=hymn_num)
