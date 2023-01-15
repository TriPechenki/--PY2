BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:

    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id_: Идентификатор книги. Задается целым положительным числом.
        :param name: Наименование книги. Ожидается получение в формате строки.
        :param pages: Кол-во страниц в книге: целое положительное число.
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть целочисленного типа(int)!")
        elif id_ <= 0:
            raise ValueError("Идентификатор книги не может быть отрицательным числом или ровняться нулю!")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Наименование книги должно быть строкой(str)!")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Кол-во страниц должно быть целочисленного типа(int)!")
        elif pages <= 0:
            raise ValueError("Кол-во страниц не может быть отрицательным числом или ровняться нулю!")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id_={self.id_}, name={self.name!r}, pages={self.pages})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
