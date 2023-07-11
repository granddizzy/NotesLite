import text_fields as tf


def main_menu() -> int:
    print(tf.menu)
    return input_choice()


def input_choice() -> int | None:
    while True:
        num = input(tf.input_choice)
        if num.isdigit() and 0 < int(num) < 13:
            return int(num)
        elif num == "":
            return None

def input_date() -> str | None:
    while True:
        date = input(tf.input_date)
        if date == "":
            return None
        elif date.replace("-", "").isdigit():
            return date


def show_notes_list(notes: list[tuple], message: str):
    if notes:
        print("\n" + "=" * 83)
        for note in notes:
            print(note[0])

        print("=" * 83 + "\n")
    else:
        print_message(message)


def show_note(note: str):
    print("\n" + "=" * 83)
    print(note)
    print("=" * 83 + "\n")


def show_book_notes(notes: list):
    print("\n" + "=" * 72)
    if len(notes) > 0:
        for note in notes:
            print(f"{str(note.id):<3} | {note.name:<20} | {note.date:<20}")
    else:
        print(tf.no_notes)
    print("=" * 72 + "\n")


def print_message(message: str):
    print("\n" + "=" * len(message))
    print(message)
    print("=" * len(message) + "\n")


def show_books(books: list):
    if len(books) == 0:
        print_message(tf.no_note_books)
    else:
        print("\n" + "=" * 72)
        for book in books:
            print(book)
        print("=" * 72 + "\n")


def select_book(books_ids):
    while True:
        num = input(tf.select_book)
        if num.isdigit() and int(num) in books_ids:
            return int(num)
        elif num == "":
            return None


def input_book():
    while True:
        if len(name := input(tf.input_book_name)) > 0:
            break

    comment = input(tf.input_book_comment)
    return name, comment


def input_note():
    while True:
        if len(name := input(tf.input_note_name)) > 0:
            break

    while True:
        if len(text := input(tf.input_note_text).replace(" ", "")) > 0:
            break

    return name, text


def select_note(notes_ids):
    while True:
        num = input(tf.select_note)
        if num.isdigit() and int(num) in notes_ids:
            return int(num)
        elif num == "":
            return None


def input_pattern():
    return input(tf.input_pattern)


def input_file():
    return input(tf.input_file_path)
