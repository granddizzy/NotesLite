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


def show_find_notes(notes: list[str], message: str):
    if notes:
        print("\n" + "=" * 83)
        for note in notes:
            print(note)

        print("=" * 83 + "\n")
    else:
        print_message(message)


def show_note(note: str):
    print("\n" + "=" * 83)
    print(note)
    print("=" * 83 + "\n")


def show_notes(notes: list):
    print("\n" + "=" * 72)
    if len(notes) > 0:
        for note in notes:
            print(f"{str(note.id):<3} | {note.name:<20} | {note.date.split('.')[0]:<20}")
    else:
        print(tf.no_notes)
    print("=" * 72 + "\n")


def print_message(message: str):
    print("\n" + "=" * len(message))
    print(message)
    print("=" * len(message) + "\n")


def input_note():
    while True:
        if len(name := input(tf.input_note_name).replace(";", "").strip()) > 0:
            break

    while True:
        if len(text := input(tf.input_note_text).replace(";", "").strip()) > 0:
            break

    return name, text

def change_note():
    name = input(tf.input_change_note_name).replace(";", "").strip()
    text = input(tf.input_change_note_text).replace(";", "").strip()

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
