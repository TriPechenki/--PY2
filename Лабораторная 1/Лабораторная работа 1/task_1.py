from typing import Union
import doctest


class Cat:
    def __init__(self, name: str, gender: str, age: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Любимый кот"
        :param name: Имя кота
        :param gender: Пол кота. Ожидается получать обозначения в виде букв "f" и "m"
        :param age: Возраст кота
        :return:

        Пример:
        >>> cat = Cat('Timofei', 'm', 1)  # инициализация экземпляра класса
        Убедитесь, что провели все ежегодные прививочные манимуляции!
        """
        if not isinstance(name, str):
            raise TypeError("Имя кота должно быть строкой(str)!")
        self.name = name

        if not (gender != "f" or gender != "m"):
            raise ValueError("Пол кота должен быть строкой(str)! Введите 'f', если это кошка, и 'm', если это кот.")
        self.gender = gender

        if not isinstance(age, (int, float)):
            raise TypeError("Возраст должен быть типа int или float!")
        elif age <= 0:
            raise ValueError("Возраст не может быть отрицательным числом или ровняться нулю!")
        self.age = age

        self.vaccination_reminder()

    def vaccination_reminder(self) -> None:
        """
        Функция выполяет проверку надобности провести коту различные вакцинации
        Запускается при каждой инициализации нового экземпляра класса и при вызове функции увеличения возраста (см. дальше)
        Так же может использоваться, если вы хотите убедиться, что коту не нужны никакие прививки

        :return: ничего не возвращает

        Пример:
        >>> cat = Cat('Musia', 'f', 0.2)  # При создании экземпляра функция запускается сама
        Ваш кот еще котенок! Убедитесь, что ему сделали все детские прививки!
        >>> # Какие-либо действия с экземпляром данного класса
        >>> cat.vaccination_reminder()  # Возникла потребность узнать потребность в проведении вакцинации
        Ваш кот еще котенок! Убедитесь, что ему сделали все детские прививки!
        """
        if self.age < 0.3:
            print("Ваш кот еще котенок! Убедитесь, что ему сделали все детские прививки!")
        elif self.age % 1 == 0:
            print("Убедитесь, что провели все ежегодные прививочные манимуляции!")

    def age_update(self, age_increase: Union[int, float]) -> None:
        """
        Функция предназначена для изменения возраста кота, кода экземпляр уже существует какое-то время
        :param age_increase: Возраст, на который кот повзрослел
        :raise ValueError: Если увеличение возраста - отрицательное число, то вызываем ошибу
        :raise TypeError: Если увеличение возраста не относится к типу int или float, то вызываем ошибу

        :return: ничего не возвращает

        Пример:
        >>> cat = Cat('Timofei', 'm', 1)
        Убедитесь, что провели все ежегодные прививочные манимуляции!
        >>> # Какие-либо действия с экземпляром данного класса
        >>> cat.age_update(2)  # Увеличение возраста кота на 2 года
        Вы изменили возраст кота, и теперь ему 3 лет
        Убедитесь, что провели все ежегодные прививочные манимуляции!
        """
        if not isinstance(age_increase, (int, float)):
            raise TypeError("Увеличение возраста должно быть типа int или float")
        elif age_increase < 0:
            raise ValueError("Увеличение возраста не может быть отрицательным числом")
        self.age += age_increase
        print(f"Вы изменили возраст кота, и теперь ему {self.age} лет")
        self.vaccination_reminder()  # Если коту требуется прививки, программа сообщит об этом

    def name_change(self, new_name: str) -> None:
        """
        Функция смены имени кота
        :param new_name: Новое имя
        :raise TypeError: Если новое имя не является строкой, то вызываем ошибу

        :return: ничего не возвращает

        Пример:
        >>> cat = Cat('Timofei', 'm', 1.7)
        >>> cat.name_change("Tima")
        Теперь кота зовут Tima
        """
        if not isinstance(new_name, str):
            raise TypeError("Новое имя кота должно быть строкой(str)!")
        self.name = new_name
        print(f"Теперь кота зовут {self.name}")


class PhonePhoto:
    def __init__(self, mode: str, zoom: int):
        """
        Создание и подготовка к работе объекта "Фото с телефона"
        :param mode: Режим съемки
        :param zoom: Увеличение при съемке

        Пример:
        >>> photo = PhonePhoto("selfie", 7)
        """
        if not isinstance(mode, str):
            raise TypeError("Режим создания фото должен быть строкой(str)!")
        self.mode = mode

        if not (isinstance(zoom, int) and 0 <= zoom <= 10):
            raise TypeError("Увеличение должено быть целым числом(int), а также должно лежать в диапазоне от 0 до 10 включительно!!")
        self.zoom = zoom

    def zoom_increase(self, increase: int) -> None:
        """
        Изменяет значение приближения, выставленное для фотографии
        Принимает положительные и отрицательные целые числа
        :param increase: Изменение приближения
        :raise TypeError: Если величина приближения не является целым цислом или не лежит в нужном диапазоне - вызываем ошибку

        :return: ничего не возвращает

        Пример:
        >>> photo = PhonePhoto("selfie", 7)
        >>> photo.zoom_increase(3)
        >>> print(photo.zoom)
        10
        """
        if not (isinstance(increase, int) and 0 <= increase + self.zoom <= 10):
            raise TypeError("Новое значение увеличения должено быть целым числом(int), а также должно лежать в диапазоне от 0 до 10 включительно!")
        self.zoom += increase

    def mode_change(self, new_mode: str) -> None:
        """
        Функция изменяет режим съемки
        :param new_mode: Новый режим съемки
        :raise ValueError: Если новый режим не является строкой, то возвращается ошибка

        :return: ничего не возвращает

        Пример:
        >>> photo = PhonePhoto("selfie", 7)
        >>> photo.mode_change("panorama")
        """
        ...


class CoffeeСup:
    def __init__(self, shot_of_espresso: int):
        """
        Создание и подготовка к работе объекта "Кофе"
        Изначально задается лишь количество подготавливаемых шотов эспрессо,
        дополнительные молоко и сахар вводятся при использовании методов данного класса
        :param shot_of_espresso: Кол-во желаемых шотов

        Пример:
        >>> coffee = CoffeeСup(2)
        """
        if not isinstance(shot_of_espresso, int):
            raise TypeError("Количество шотов должно быть целым(int) числом!")
        elif shot_of_espresso <= 0:
            raise ValueError("Количество шотов должно быть положительным числом!")
        self.shot_of_espresso = shot_of_espresso
        self.portion_of_milk = None
        self.sugar_cube = None

    def addition_milk(self, milk: int) -> None:
        """
        Функция задает значение добавленных порций молока
        :param milk: Добавление порций молока
        :raise ValueError: Если количество добавляемых порций является отрицательным, то вызываем ошибку

        :return: ничего не возвращает

        Пример:
        >>> coffee = CoffeeСup(1)
        >>> print(coffee.portion_of_milk)
        None
        >>> coffee.addition_milk(1)
        >>> print(coffee.portion_of_milk)
        1
        """
        if milk <= 0:
            raise ValueError("Количество молока должно быть положительным числом!")
        self.portion_of_milk = milk

    def addition_sugar(self, sugar: int) -> None:
        """
        Функция задает значение добавленных порций сахара
        :param sugar:  Добавление порций сахара
        :raise ValueError: Если количество добавляемых порций является отрицательным, то вызываем ошибку

        :return: ничего не возвращает

        Пример:
        >>> coffee = CoffeeСup(2)
        >>> print(coffee.sugar_cube)
        None
        >>> coffee.addition_sugar(2)
        >>> print(coffee.sugar_cube)
        2
        """
        if sugar <= 0:
            raise ValueError("Количество сахара должно быть положительным числом!")
        self.sugar_cube = sugar


if __name__ == "__main__":
    doctest.testmod()
