from Database.DB import ClassDB
from datetime import datetime


class Note:
    def __init__(self, database: ClassDB, book_id: int, id: int, name: str, text: str, date: str):
        self.date = date
        self.id = id
        self.name = name
        self.text = text
        self.book_id = book_id
        self.db = database

    def __str__(self):
        return f"{'Идентификатор:':<15} {self.id}\n{'Дата изменения:':<15} {self.date}\n{'Наименование:':<15} {self.name:<20}\n{'Текст:':<15} {self.text:<20}\n{'Книга:':<15} {self.book_id:<20}"

    def get_dump(self):
        return {"id": self.id, "name": self.name, "text": self.text}

    def update_db(self):
        self.db.update_data("notes", {"name": self.name, "text": self.text, "data": str(datetime.now())},
                            {"note_id": self.id})

    def delete(self):
        self.db.delete_data("notes", {"note_id": self.id})


class Book:
    def __init__(self, database: ClassDB, book_id: int, name: str, comment: str):
        self.id = book_id
        self.db = database
        self.name = name
        self.comment = comment

    def get_note(self, id) -> Note:
        name, text, date = self.db.get_data("notes", ("name", "text", "date"), {"note_id": id})
        return Note(self.db, self.id, id, name, text, date)

    def get_note_list(self, date: str | None = None) -> list[Note]:
        if date:
            return [Note(self.db, *item) for item in
                    self.db.get_data("notes", ("book_id", "note_id", "name", "text, date"),
                                     {"book_id": self.id, "date": '%' + date + '%'}, fetchall=True, like=True,
                                     or_and="AND")]
        else:
            return [Note(self.db, *item) for item in
                    self.db.get_data("notes", ("book_id", "note_id", "name", "text, date"),
                                     {"book_id": self.id}, fetchall=True)]

    def get_notes_ids(self) -> list[int]:
        return [item[1] for item in self.db.get_data("notes", ("book_id", "note_id", "name", "text"),
                                                     {"book_id": self.id}, fetchall=True)]

    def __str__(self):
        return f"{self.id:<3} | {self.name:<20} | {self.comment:<20}"

    def update_db(self):
        self.db.update_data("books", {"name": self.name, "comment": self.comment}, {"book_id": self.id})

    def del_book(self):
        self.db.delete_data("notes", {"book_id": self.id})
        self.db.delete_data("books", {"book_id": self.id})

    def add_note(self, name: str, text: str):
        self.db.insert_data("notes", {"name": name, "text": text, "book_id": self.id, "date": str(datetime.now())})

    def clear(self):
        for note in self.get_note_list():
            self.db.delete_data("notes", {"notes_id": note.id})
