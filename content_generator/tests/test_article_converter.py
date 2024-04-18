from content_generator.src.article_converter import ArticleConverter


def test_base_converting():
    converter = ArticleConverter()
    assert converter.convert("test") == "test"