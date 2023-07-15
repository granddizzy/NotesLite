from Database import ClassDB2
from classes import Note
from datetime import datetime
import json

db = ClassDB2()


def find_notes(pattern) -> list[Note]:
    return [Note(db, *item) for item in
            db.get_data("notes", ("note_id", "name", "text", "date"),
                        {"name": '%' + pattern + '%', "text": '%' + pattern + '%'},
                        fetchall=True, like=True, or_and="OR")]


def get_note_list(date: str | None = None) -> list[Note]:
    if date:
        return [Note(db, *item) for item in
                db.get_data("notes", ("book_id", "note_id", "name", "text", "date"),
                            {"book_id": id, "date": '%' + date + '%'}, fetchall=True, like=True,
                            or_and="AND")]
    else:
        return [Note(db, *item) for item in
                db.get_data("notes", ("note_id", "name", "text", "date"), fetchall=True)]


def get_notes_ids() -> list[int]:
    return [int(item[0]) for item in db.get_data("notes", ("note_id", "name", "text", "date"), fetchall=True)]


def get_note(id) -> Note:
    name, text, date = db.get_data("notes", ("name", "text", "date"), {"note_id": id})
    return Note(db, id, name, text, date)


def add_note(name: str, text: str):
    db.insert_data("notes", {"name": name, "text": text, "date": str(datetime.now())})
