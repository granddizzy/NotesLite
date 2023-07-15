class ClassDB2:
    def __init__(self, db_path: str = "Database/notes.csv"):
        self.db_path = db_path

        self.noteFields = {}
        self.noteFields["note_id"] = 0
        self.noteFields["name"] = 1
        self.noteFields["text"] = 2
        self.noteFields["date"] = 3

        with open(self.db_path, "a", encoding="UTF-8") as file:
            pass

    @staticmethod
    def extract_kwargs(querry: str, parameters: dict) -> tuple:
        querry += " AND ".join(f"{key} = ?" for key in parameters)
        return querry, tuple(parameters.values())

    def get_data(self, table: str, fields: tuple, conditions=None, fetchall: bool = False, like: bool = False,
                 or_and: str = "AND"):
        res = []
        if table == "notes":
            with open(self.db_path, "r", encoding="UTF-8") as file:
                data = file.readlines()

                for line in data:
                    arr_line = line.replace("\n", "").split(";")
                    need_add = True

                    if conditions:
                        for condition in conditions.keys():
                            if arr_line[self.noteFields[condition]] != str(conditions[condition]):
                                need_add = False
                                break

                    if not need_add:
                        continue

                    if fetchall:
                        res.append(tuple([arr_line[self.noteFields[item]] for item in fields]))
                    else:
                        res += [arr_line[self.noteFields[item]] for item in fields]
                        break

        return res

    def delete_data(self, table: str, conditions=None, or_and: str = "AND"):
        if table == "notes":
            with open(self.db_path, "r", encoding="UTF-8") as file:
                data = file.readlines()

            with open(self.db_path, "w", encoding="UTF-8") as file:
                for line in data:
                    need_save = True
                    arr_line = line.replace("\n", "").split(";")

                    if conditions:
                        for condition in conditions.keys():
                            if arr_line[self.noteFields[condition]] == str(conditions[condition]):
                                need_save = False
                                break
                    else:
                        need_save = False

                    if need_save:
                        print(line, end="", file=file)

    def update_data(self, table: str, fields: dict, conditions=None, or_and: str = "AND"):
        if not conditions:
            return

        if table == "notes":
            with open(self.db_path, "r", encoding="UTF-8") as file:
                data = file.readlines()

            with open(self.db_path, "w", encoding="UTF-8") as file:
                for line in data:
                    arr_line = line.replace("\n", "").split(";")

                    for condition in conditions.keys():
                        if arr_line[self.noteFields[condition]] == str(conditions[condition]):



                            print(, end="", file=file)
                            break
                    else:
                        print(line, end="", file=file)


def insert_data(self, table: str, fields: dict):
    if table == "notes":
        with open(self.db_path, "a", encoding="UTF-8") as file:
            print(str(self.get_new_id()) + ";" + ";".join(fields.values()), file=file)


def get_new_id(self) -> int:
    with open(self.db_path, "r", encoding="UTF-8") as file:
        date = file.readlines()

        if len(date) == 0:
            return 1
        else:
            return int(date[len(date) - 1].split(";")[0]) + 1
