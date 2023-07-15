import view
import model
import text_fields as tf


def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                # просмотр заметок
                date = view.input_date()
                view.show_notes(model.get_note_list(date))
            case 2:
                # открыть заметку
                view.show_notes(model.get_note_list())
                id = view.select_note(model.get_notes_ids())
                if id:
                    note = model.get_note(id)
                    view.show_note(str(note))
            case 3:
                pass
                # найти заметку
                view.show_find_notes(
                    [(str(note),) for note in model.find_notes(view.input_pattern())], message=tf.no_find_notes)
            case 4:
                # создать заметку
                model.add_note(*view.input_note())
                view.show_notes(model.get_note_list())
            case 5:
                # изменить заметку
                view.show_notes(model.get_note_list())
                id = view.select_note(model.get_notes_ids())
                if id:
                    note = model.get_note(id)
                    note.name, note.text = view.input_note()
                    note.update_db()
                    view.show_notes(model.get_note_list())
            case 6:
                # удалить заметку
                view.show_notes(model.get_note_list())
                id = view.select_note(model.get_notes_ids())
                if id:
                    note = model.get_note(id)
                    model.get_note(id).delete()
                    view.print_message(tf.sucessfull_delete_note.replace("%name%", note.name))
                    view.show_notes(model.get_note_list())
            case _:
                break
