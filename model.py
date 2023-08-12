from classes import Note
from datetime import datetime
import os

db_path = "notes.csv"

if not os.path.exists(db_path):
    with open(db_path, "w", encoding="UTF-8") as file:
        pass


def find_notes(pattern) -> list[Note]:
    """
    возвращает список заметок в которых заголовок или текст содержит заданный шаблон
    :param pattern:
    :return:
    """

    res = []
    with open(db_path, "r", encoding="UTF-8") as file:
        data = file.readlines()

        for line in data:
            arr_line = line.replace("\n", "").split(";")

            if pattern and (pattern in arr_line[1] or pattern in arr_line[2]):
                res.append(Note(*arr_line))

    return res


def get_note_list(date: str | None = None) -> list[Note]:
    """
    возвращает список заметок определенную дату или все если дата не указана
    :param date:
    :return:
    """

    res = []
    with open(db_path, "r", encoding="UTF-8") as file:
        data = file.readlines()

        for line in data:
            arr_line = line.replace("\n", "").split(";")

            if date and arr_line[3].split()[0] != date:
                continue

            res.append(Note(*arr_line))

    return res


def get_notes_ids() -> list[int]:
    """
    возвращает список идентификаторов заметок
    :return:
    """

    res = []
    with open(db_path, "r", encoding="UTF-8") as file:
        data = file.readlines()

        for line in data:
            arr_line = line.replace("\n", "").split(";")
            res.append(int(arr_line[0]))

    return res


def get_note(id: int) -> Note | None:
    """
    возвращает заметку с заданным ID
    :param id:
    :return:
    """

    with open(db_path, "r", encoding="UTF-8") as file:
        data = file.readlines()

        for line in data:
            arr_line = line.replace("\n", "").split(";")
            if id and str(id) == line[0]:
                return Note(*arr_line)

    return None


def add_note(name: str, text: str):
    """
    добавляет заметку
    :param name:
    :param text:
    :return:
    """

    with open(db_path, "a", encoding="UTF-8") as file:
        print(str(get_new_id()) + ";" + name + ";" + text + ";" + str(datetime.now()), file=file)


def get_new_id() -> int:
    """
    возвращает следующий идентификатор для заметки
    :return:
    """

    with open(db_path, "r", encoding="UTF-8") as file:
        date = file.readlines()
        if len(date) == 0:
            return 1
        else:
            return int(date[len(date) - 1].split(";")[0]) + 1


def delete(id: int):
    """
    удаляет заметку с заданным ID
    :param id:
    :return:
    """

    if not id:
        return

    with open(db_path, "r", encoding="UTF-8") as file:
        data = file.readlines()

    with open(db_path, "w", encoding="UTF-8") as file:
        for line in data:
            need_save = True
            arr_line = line.replace("\n", "").split(";")

            if id == int(arr_line[0]):
                continue

            if need_save:
                print(line, end="", file=file)


def update(note: Note):
    """
    обновляет данные заметки
    :param note: 
    :return:
    """

    with open(db_path, "r", encoding="UTF-8") as file:
        data = file.readlines()

    with open(db_path, "w", encoding="UTF-8") as file:
        for line in data:
            arr_line = line.replace("\n", "").split(";")

            if note.id == int(arr_line[0]):
                print(str(note.id) + ";" + note.name + ";" + note.text + ";" + str(datetime.now()), end="\n", file=file)
            else:
                print(line, end="", file=file)
