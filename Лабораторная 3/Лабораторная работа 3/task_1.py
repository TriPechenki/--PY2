class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Инициализация объекта книга
        :param name: Название книги
        :param author: Имя автора книги

        Пример:
        >>> book = Book("Гордость и предубеждение", "Джейн Остин")
        >>> print(book)
        Книга Гордость и предубеждение. Автор Джейн Остин
        >>> print(repr(book))
        Book(name='Гордость и предубеждение', author='Джейн Остин')
        """
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    """ Дочерний класс Бумажные книги. """
    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация объекта бумажная книга
        :param name: Название книги
        :param author: Имя автора книги
        :param pages: Количество страниц книги

        Пример:
        >>> book = PaperBook("Гордость и предубеждение", "Джейн Остин", 416)
        >>> print(book)
        Книга Гордость и предубеждение. Автор Джейн Остин
        >>> print(repr(book))
        PaperBook(name='Гордость и предубеждение', author='Джейн Остин', pages=416)
        """
        super().__init__(name=name, author=author)
        self._pages = pages

    # Поскольку метод __repr__ должен возвращать строку, показывающую,как может быть инициализирован экземпляр, его следует перегрузить в дочерних классах. А метод __str__ может наследоваться из родительского класса, т.к. дает основную информацию о книге вне зависимости от того, бумажная она или "звуковая"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Число страниц должно быть целочисленного типа (int)!")
        elif new_pages <= 0:
            raise ValueError("Число страниц должно быть положительным числом!")
        self._pages = new_pages


class AudioBook(Book):
    """ Дочерний класс Аудиокниги. """
    def __init__(self, name: str, author: str, duration: float):
        """

        :param name: Название аудиокниги
        :param author: Имя автора книги
        :param duration: Продолжительность аудиокниги(в часах)

        Пример:
        >>> book = AudioBook("Гордость и предубеждение", "Джейн Остин", 20.6)
        >>> print(book)
        Книга Гордость и предубеждение. Автор Джейн Остин
        >>> print(repr(book))
        AudioBook(name='Гордость и предубеждение', author='Джейн Остин', duration=20.6)
        """
        super().__init__(name=name, author=author)
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть целочисленного типа (int)!")
        elif new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом!")
        self._duration = new_duration
