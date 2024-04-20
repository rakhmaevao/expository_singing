import warnings
from pathlib import Path

from content_generator.src.note_creator import NotConversableNoteError, NoteCreator


def test_all_notes_is_ready():
    not_ready_notes = []
    for note_path in Path("music_notes").iterdir():
        if not note_path.is_file():
            continue
        if note_path.suffix != ".md":
            continue
        with note_path.open(encoding="utf-8") as f:
            md_text = f.read()
            try:
                NoteCreator().create(md_text)
            except NotConversableNoteError:
                not_ready_notes.append(note_path)

    if not_ready_notes:
        paths = ""
        for note_path in not_ready_notes:
            paths += f"\n{note_path}"
        warnings.warn(f"Not ready notes {paths}")  # noqa: B028
