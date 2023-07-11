import sqlite3


class ClassDB:
    def __init__(self, db_path: str = "Database/book.db"):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, querry: str, parametrs: tuple = tuple(), fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None

        try:
            cursor.execute(querry, parametrs)
        except:
            print(f"DB QUERY FAILURE:\n{querry}")
            print(parametrs)

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    @staticmethod
    def extract_kwargs(querry: str, parameters: dict) -> tuple:
        querry += " AND ".join(f"{key} = ?" for key in parameters)
        return querry, tuple(parameters.values())

    def disconnect(self):
        self.connection.close()

    def get_data(self, table: str, fields: tuple, conditions=None, fetchall: bool = False, like: bool = False,
                 or_and: str = "AND"):
        if conditions is not None:
            sign = " LIKE " if like else "="
            query_conditions = f"WHERE {f' {or_and} '.join(f'{key}{sign}?' for key in conditions.keys())}"
        else:
            query_conditions = ""

        query = f"""SELECT {', '.join(fields) if len(fields) > 1 else fields[0]} FROM {table} {query_conditions}"""

        if conditions is None:
            parameters = ()
        else:
            parameters = tuple(conditions.values())

        return self.execute(query, parameters, fetchall=fetchall, fetchone=not fetchall)

    def delete_data(self, table: str, conditions=None, or_and: str = "AND"):
        if conditions is not None:
            query_conditions = f"WHERE {f' {or_and} '.join(f'{key}=?' for key in conditions.keys())}"
        else:
            query_conditions = ""

        query = f"""DELETE FROM {table} {query_conditions}"""

        if conditions is None:
            parameters = ()
        else:
            parameters = tuple(conditions.values())

        return self.execute(query, parameters, commit=True)

    def update_data(self, table: str, fields: dict, conditions=None, or_and: str = "AND"):
        if conditions is not None:
            query_conditions = f"WHERE {f' {or_and} '.join(f'{key}=?' for key in conditions.keys())}"
        else:
            query_conditions = ""

        query = f"""UPDATE {table} SET {', '.join(map(lambda x: x + '=?', fields.keys())) if len(fields) > 1 else fields[0] + '=?'} {query_conditions}"""

        if conditions is None:
            parameters = ()
        else:
            parameters = tuple(fields.values()) + tuple(conditions.values())

        return self.execute(query, parameters, commit=True)

    def insert_data(self, table: str, fields: dict):
        query = f"""INSERT INTO {table} ({', '.join(fields.keys()) if len(fields) > 1 else fields[0]}) VALUES ({', '.join(["?" for _ in fields.keys()])})"""
        return self.execute(query, tuple(fields.values()), commit=True)


def create_tables(db_: ClassDB):
    query = """CREATE TABLE IF NOT EXISTS books (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name VARCHAR, comment VARCHAR)"""
    db_.execute(query)

    query = """CREATE TABLE IF NOT EXISTS notes (note_id INTEGER PRIMARY KEY AUTOINCREMENT,
          book_id INTEGER, name VARCHAR, text VARCHAR, date TEXT)"""
    db_.execute(query)
