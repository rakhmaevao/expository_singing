from pathlib import Path

from src.notes_converter import NotesConverter

if __name__ == "__main__":
    NotesConverter().convert(Path("music_notes"), Path("content/Гимны"))
