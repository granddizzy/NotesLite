class Note:
    def __init__(self, id: int, name: str, text: str, date: str):
        self.id = int(id)
        self.name = name
        self.text = text
        self.date = date

    def __str__(self):
        return f"{'Идентификатор:':<15} {self.id}\n{'Дата изменения:':<15} {self.date.split('.')[0]}\n{'Заголовок:':<15} {self.name:<20}\n{'Содержание:':<15} {self.text:<20}"

