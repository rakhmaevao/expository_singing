from pathlib import Path

from src.home_generator import generate_home
from src.notes_converter import NotesConverter

if __name__ == "__main__":
    hymn_number = NotesConverter().convert(Path("music_notes"), Path("content/Гимны"))
    home_body = generate_home(hymn_number)
    with Path("content/pages/home.md").open("w", encoding="utf-8") as f:
        f.write(home_body)
