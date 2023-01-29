from typing import Union

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

        :param id_: Идентификатор книги. Задается целым положительным числом
        :param name: Наименование книги. Ожидается получение в формате строки
        :param pages: Кол-во страниц в книге: целое положительное число
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


class Library:
    def __init__(self, books: Union[None, list] = None):
        """
        Подготовка к работе объекта "Библиотека"

        :param books: Список книг с указанными соответствующими данными об их идентификационном номере, авторе и количестве страниц
        По-умолчанию значение задается как пустой список
        """
        if books is not None and not isinstance(books, list):
           raise TypeError("Некорректный тип атрибута books. Список Книг должен быть списком(list) или же None!")
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Метод, позволяющий получить индекс для книги, которую требуется добавить в библиотеку: книга получает  индекс на единицу больше, чем у последней добавленной книги
        В случае,если книги в списке отсутсвуют, новая книга получает индекс 1
        :return: индекс для новой книги
        """
        if self.books is None:
            return 1
        else:
            return self.books[-1].id_+1

    def get_index_by_book_id(self, fined_id: int):
        """
        Метод выполняет поиск книги по заданному идентификационному номеру
        Если книги с данным номером не существует - выводится сообщение об ошибке
        :param fined_id: Id книги, которую требуется найти
        :return: индекс положения книги в списке
        """
        id_index = None
        if self.books is None:
            self.books = []
        for number, book in enumerate(self.books):
            if book.id_ == fined_id:
                id_index = number
        if id_index == None:
            raise ValueError('Книги с запрашиваемым id не существует')
        else:
            return id_index


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
