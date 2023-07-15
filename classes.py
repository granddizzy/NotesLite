from Database.DB_SQLITE3 import ClassDB
from datetime import datetime


class Note:
    def __init__(self, database: ClassDB, id: int, name: str, text: str, date: str):
        self.id = id
        self.name = name
        self.text = text
        self.date = date
        self.db = database

    def __str__(self):
        return f"{'Идентификатор:':<15} {self.id}\n{'Дата изменения:':<15} {self.date}\n{'Заголовок:':<15} {self.name:<20}\n{'Содержание:':<15} {self.text:<20}\n"

    # def get_dump(self):
    #     return {"id": self.id, "name": self.name, "text": self.text, "date": self.date}

    def update_db(self):
        self.db.update_data("notes", {"name": self.name, "text": self.text, "date": str(datetime.now())},
                            {"note_id": self.id})

    def delete(self):
        self.db.delete_data("notes", {"note_id": self.id})