from pathlib import Path

from transliterate import slugify

from .note_creator import NotConversableNoteError, NoteCreator


class BadPathError(Exception):
    def __init__(self) -> None:
        super().__init__("src and dst must be directories")


class NotesConverter:
    def convert(self, src: Path, dst: Path) -> None:
        if not src.is_dir() or not dst.is_dir():
            raise BadPathError

        for note_path in src.iterdir():
            if not note_path.is_file():
                continue
            if note_path.suffix != ".md":
                continue
            with note_path.open(encoding="utf-8") as f:
                md_text = f.read()
                try:
                    note = NoteCreator().create(md_text)
                except NotConversableNoteError:
                    continue
            new_filename = slugify(note.title) + ".md"
            with (dst / new_filename).open("w", encoding="utf-8") as f:
                f.write(note.content)
