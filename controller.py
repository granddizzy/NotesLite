import view
import model
import text_fields as tf


def start():
    model.create_db_tables()

    while True:
        if model.get_curr_book():
            view.print_message(tf.current_book.replace("%name%", model.get_curr_book().name))
        else:
            view.print_message(tf.no_note_book)

        choice = view.main_menu()
        match choice:
            case 1:
                # выбрать книгу
                books = model.get_books_list()
                view.show_books(list(map(str, books)))
                if len(books) > 0:
                    book_id = view.select_book([book.id for book in model.get_books_list()])
                    if book_id:
                        model.set_curr_book(book_id)
            case 2:
                # создать книгу
                view.show_books(list(map(str, model.get_books_list())))
                name, comment = view.input_book()
                model.create_book(name, comment)
                view.print_message(tf.sucessfull_create_book.replace("%name%", name))
            case 3:
                # изменить книгу
                if model.get_curr_book():
                    book = model.get_curr_book()
                    book.name, book.comment = view.input_book()
                    book.update_db()
                    view.show_books(list(map(str, model.get_books_list())))
            case 4:
                # удалить книгу
                if model.get_curr_book():
                    book = model.get_curr_book()
                    book.del_book()
                    view.print_message(tf.sucessfull_delete_book.replace("%name%", book.name))
                    view.show_books(list(map(str, model.get_books_list())))
                    model.set_curr_book(None)
            case 5:
                # просмотр записок
                if model.get_curr_book():
                    date = view.input_date()
                    view.show_book_notes(model.get_curr_book().get_note_list(date))
            case 6:
                # открыть записку
                if model.get_curr_book():
                    view.show_book_notes(model.get_curr_book().get_note_list())
                    id = view.select_note(model.get_curr_book().get_notes_ids())
                    if id:
                        note = model.get_curr_book().get_note(id)
                        view.show_note(str(note))
            case 7:
                # найти записку
                view.show_notes_list(
                    [(str(note), note.book_id) for note in model.find_notes(view.input_pattern())],
                    message=tf.no_find_notes)
            case 8:
                # создать записку
                if model.get_curr_book():
                    model.get_curr_book().add_note(*view.input_note())
                    view.show_book_notes(model.get_curr_book().get_note_list())
            case 9:
                # изменить записку
                if model.get_curr_book():
                    view.show_book_notes(model.get_curr_book().get_note_list())
                    id = view.select_note(model.get_curr_book().get_notes_ids())
                    if id:
                        note = model.get_curr_book().get_note(id)
                        note.name, note.text, note.comment = view.input_note()
                        note.update_db()
                        view.show_book_notes(model.get_curr_book().get_note_list())
            case 10:
                # удалить записку
                if model.get_curr_book():
                    view.show_book_notes(model.get_curr_book().get_note_list())
                    id = view.select_note(model.get_curr_book().get_notes_ids())
                    if id:
                        note = model.get_curr_book().get_note(id)
                        model.get_curr_book().get_note(id).delete()
                        view.print_message(tf.sucessfull_delete_note.replace("%name%", note.name))
                        view.show_book_notes(model.get_curr_book().get_note_list())
            case 11:
                # сохранить книгу в файл
                if model.get_curr_book():
                    path = view.input_file()
                    if path:
                        model.save_book_in_file(path)
            case 12:
                # загрузить книгу из файла
                if model.get_curr_book():
                    path = view.input_file()
                    if path:
                        if not model.load_book_from_file(path):
                            view.print_message(tf.error_book_load)
            case _:
                break
