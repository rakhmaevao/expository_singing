from pathlib import Path
from .note_converter import NotConversableNoteError, NoteConverter
from transliterate import slugify

class NotesConverter:

    def convert(self, src: Path, dst: Path) -> None:
        if not src.is_dir() or not dst.is_dir():
            raise ValueError("src and dst must be directories")
        
        for note in src.iterdir():
            if not note.is_file():
                continue
            if not note.suffix == ".md":
                continue
            with open(note, "r", encoding="utf-8") as f:
                md_text = f.read()
                try:
                    note = NoteConverter().convert(md_text)
                except NotConversableNoteError:
                    continue
            new_filename = slugify(note.title) + ".md"
            with open(dst / new_filename, "w", encoding="utf-8") as f:
                f.write(note.content)