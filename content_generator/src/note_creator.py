import re

from loguru import logger

from .note import Note


class NotConversableNoteError(Exception):
    pass


class NoteCreator:
    _NEED_LEN_RAW_PROP = 2

    def __init__(self):
        pass

    def create(self, md_text: str) -> Note:
        if not md_text.startswith("---"):
            raise NotConversableNoteError
        body = md_text.split("---")[2]
        tags = self.__get_tags(body)
        if "#raw" in tags:
            raise NotConversableNoteError
        obsidian_properties = self._get_obsidian_properties(md_text)
        for tag in tags:
            body = body.replace(tag, "")
        body = self._get_hat(obsidian_properties) + body
        return Note(title=obsidian_properties["title"], content=body)

    def _get_obsidian_properties(self, md_text: str) -> dict:
        raw_properties = md_text.split("---")[1].split("---")[0]
        properties: dict = {}
        for raw_property in raw_properties.split("\n"):
            raw_properties_items = raw_property.split(": ")
            if len(raw_properties_items) < self._NEED_LEN_RAW_PROP:
                continue
            key = raw_properties_items[0]
            value = raw_properties_items[1]
            if value.startswith("[[") and value.endswith("]]"):
                value = value[2:-2]
            properties[key] = value
        return properties

    def __get_tags(self, body: str) -> list[str]:
        return re.findall(r"#\w+", body)

    def _get_hat(self, properties: dict) -> str:
        if "title" not in properties:
            logger.error(f"No title in properties: {properties}")
        hat = (
            f'Title: {properties["title"]}\n'
            "Date: 1993-06-12\n"
            "Categories: Гимны\n\n"
        )
        mapping = {
            "original_title": "Оригинальное название",
            "poet": "Поэт",
            "translator": "Переводчик",
            "composer": "Композитор",
            "song_of_rebirth": "Песнь возрождения",
            "published": "Дата написания",
        }
        for prop in properties:
            if prop in mapping:
                hat += f"{mapping[prop]}: {properties[prop]}\n\n"
        return hat
