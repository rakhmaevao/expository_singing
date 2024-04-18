class ArticleConverter:
    def __init__(self):
        pass

    def convert(self, md_text: str) -> str:
        obsidian_tags = self._get_obsidian_tags(md_text)

    def _get_obsidian_tags(self, md_text: str) -> dict:
        raw_tags = md_text.split("---")[1].split("---")[0]
        tags: dict = {}
        for raw_tag in raw_tags.split("\n"):
            raw_tags_items = raw_tag.split(": ")
            if len(raw_tags_items) < 2:
                continue
            key = raw_tags_items[0]
            value = raw_tags_items[1]
            if value.startswith('"[[') and value.endswith(']]"'):
                value = value[3:-3]
            tags[key] = value
        return tags
