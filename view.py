import text_fields as tf


def main_menu() -> int:
    """
    Показывает главное меню
    :return:
    """

    print(tf.menu)
    return input_choice()


def input_choice() -> int | None:
    """
    Предлагает сделать выбор
    :return:
    """

    while True:
        num = input(tf.input_choice)
        if num.isdigit() and 0 < int(num) < 13:
            return int(num)
        elif num == "":
            return None


def input_date() -> str | None:
    """
    Предлагает ввести дату
    :return:
    """

    while True:
        date = input(tf.input_date)
        if date == "":
            return None
        elif date.replace("-", "").isdigit():
            return date


def show_find_notes(notes: list[str], message: str):
    """
    Выводит список найденных по шаблону заметок
    :param notes:
    :param message:
    :return:
    """

    if notes:
        print("\n" + "=" * 83)
        for note in notes:
            print(note)

        print("=" * 83 + "\n")
    else:
        print_message(message)


def show_note(note: str):
    """
    Выводит данные заметки
    :param note:
    :return:
    """

    print("\n" + "=" * 83)
    print(note)
    print("=" * 83 + "\n")


def show_notes(notes: list):
    """
    Выводит переданный список заметок
    :param notes:
    :return:
    """

    print("\n" + "=" * 72)
    if len(notes) > 0:
        for note in notes:
            print(f"{str(note.id):<3} | {note.name:<20} | {note.date.split('.')[0]:<20}")
    else:
        print(tf.no_notes)
    print("=" * 72 + "\n")


def print_message(message: str):
    """
    Выводит сообщение
    :param message:
    :return:
    """

    print("\n" + "=" * len(message))
    print(message)
    print("=" * len(message) + "\n")


def input_note():
    """
    Предлагает ввести заголовок и текст новой заметки
    :return:
    """

    while True:
        if len(name := input(tf.input_note_name).replace(";", "").strip()) > 0:
            break

    while True:
        if len(text := input(tf.input_note_text).replace(";", "").strip()) > 0:
            break

    return name, text

def change_note():
    """
    Предлагает ввести заголовок и текст для изменения заметки
    :return:
    """

    name = input(tf.input_change_note_name).replace(";", "").strip()
    text = input(tf.input_change_note_text).replace(";", "").strip()

    return name, text


def select_note(notes_ids):
    """
    Предлагает ввести идентификатор заметки из списка идентификаторов
    :param notes_ids:
    :return:
    """

    while True:
        num = input(tf.select_note)
        if num.isdigit() and int(num) in notes_ids:
            return int(num)
        elif num == "":
            return None


def input_pattern():
    """
    Предлагает ввести шаблон для поиска
    :return:
    """

    return input(tf.input_pattern)

