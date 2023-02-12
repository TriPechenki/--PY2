class Clothes:
    """ Базовый класс Одежда. """
    MALE_INTERNATIONAL_SIZE = {44: "XS", 46: "S", 48: "M",  50: "L", 52: "XL", 54: "XXL", 56: "XXXL", 58: "4XL", 60: "5XL", 62: "5XL"}
    FEMALE_INTERNATIONAL_SIZE = {40: "XS", 42: "S", 44: "S", 46: "M", 48: "M", 50: "L", 52: "L", 54: "XL", 56: "XXL", 58: "XXXL", 60: "4XL"}
    def __init__(self, brand_name: str, gender: str, size: int):
        """
        Инициализация объекта Одежда
        :param brand_name: Наименование бренда/организации производителя
        :param gender: Отношение типа одежды к мужскому (M/m) или женскому (F/f) отделу
        :param size: Размер изделия. Для женских изделий 40-60 (Международная сетка: 40= "XS", 42= "S", 44= "S", 46= "M", 48= "M", 50= "L", 52= "L", 54= "XL", 56= "XXL", 58= "XXXL", 60= "4XL"), для мужских 44-62 (Международная сетка: 44= "XS", 46= "S", 48= "M",  50= "L", 52= "XL", 54= "XXL", 56= "XXXL", 58= "4XL", 60= "5XL", 62= "5XL")
        Все атрибуты родительского класса являются непубличными и не подлежат изменению после инициализации класса
        """
        if not isinstance(brand_name, str):
            raise TypeError("Название бренда производителя должно иметь формат строки!")
        self._brand_name = brand_name
        if not (gender == "M" or gender == "m" or gender == "F" or gender == "f"):
            raise ValueError("Некорректно указан тип одежды (мужская - M, m/ женская - F, f)! ")
        self._gender = gender
        if not isinstance(size, int):
            raise TypeError("Размер изделия должен являться целым числом!")
        elif gender == "M" or gender == "m":
            if not 44 <= size <= 62 and size % 2 == 0:
                raise ValueError("Указанное значение не входит в размерную сетку мужской одежды (44 - 62 размер)!")
        elif not gender == "F" or gender == "f":
            if not 40 <= size <= 60 and size % 2 == 0:
                raise ValueError("Указанное значение не входит в размерную сетку женской одежды (40 - 60 размер)!")
        self._size = size

    def __str__(self):
        """
        Не перегружается в дочерних классах, так как содержит лишь основнуюинформацию о положении изделия в системе.
        :return:
        """
        return f"Изделие бренда {self._brand_name}. Отдел {self._gender}. Размер {self._size}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand_name={self._brand_name!r}, gender={self._gender!r}, size={self._size!r})"

    def conversion_to_international_size(self) -> None:
        """
        Метод, позволяющий получить информацию о размере данного изделия в международной сетке. Наследуется для всех дочерних классов.
        :return: ничего не возвращает
        """
        if self._gender == "M" or self._gender == "m":
            print(f"В международной сетке размеров данное изделие имеет размер {self.MALE_INTERNATIONAL_SIZE[self._size]}")
        elif self._gender == "F" or self._gender == "f":
            print(f"В международной сетке размеров данное изделие имеет размер {self.FEMALE_INTERNATIONAL_SIZE[self._size]}")

    def washing_mode_information(self) -> None:
        """
        Метод, позволяющий получить информацию по рекомендуемым режимам стирки для изделий. Перегружается в тех дочерних классах, для изделий которых необходимы особые режимы стирки.
        :return: ничего не возвращает
        """
        print("Белые вещи можно стирать при температуре до 65 °C, для цветных изделий подходит температура от 30 до 40 °C (при стирке в горячей воде одежда может выцвести). Оптимальный режим отжима — до 800 оборотов в минуту. Цветные и белые вещи стирайте отдельно. Прежде чем положить одежду в машинку, проверьте, не линяет ли она.")

class ClothesFromDelicateFabric(Clothes):
    """Дочерний класс Одежда из деликатных типов ткани"""
    DELICAT_FABRIC =["Кашемир", "Шелк", "Вискоза", "Лён", "Шерсть", "Микрофибра"]
    def __init__(self, brand_name: str, gender: str, size: int, fabric: str):
        """
        Инициализация объекта Одежда из деликатных типов ткани
        :param brand_name: Наименование бренда/организации производителя
        :param gender: Отношение типа одежды к мужскому (M/m) или женскому (F/f) отделу
        :param size: Размер изделия. Для женских изделий 40-60 (Международная сетка: 40= "XS", 42= "S", 44= "S", 46= "M", 48= "M", 50= "L", 52= "L", 54= "XL", 56= "XXL", 58= "XXXL", 60= "4XL"), для мужских 44-62 (Международная сетка: 44= "XS", 46= "S", 48= "M",  50= "L", 52= "XL", 54= "XXL", 56= "XXXL", 58= "4XL", 60= "5XL", 62= "5XL")
        :param fabric: Тань изделия. Данный класс инициализирует объекты ТОЛЬКО из следующих типов ткани: "Кашемир", "Шелк", "Вискоза", "Лён", "Шерсть", "Микрофибра"
        """
        super().__init__(brand_name=brand_name, gender=gender, size=size)
        if not isinstance(fabric, str):
            raise TypeError("Название такани изделия должно иметь формат сроки!")
        elif fabric not in self.DELICAT_FABRIC:
            raise ValueError(f"{fabric} не относится к установленному перечню деликатных тканей!")
        self.fabric = fabric

    def __repr__(self):
        """
        Метод перегружен в связи с изменением кол-ва атрибутов объекта в дочернем классе
        :return:
        """
        return f"{self.__class__.__name__}(brand_name={self._brand_name!r}, gender={self._gender!r}, size={self._size!r}, fabric={self.fabric!r})"

    def washing_mode_information(self) -> None:
        """
        Метод перегружен, т.к. изделия из деликатных типов ткани требуют осторожной стирки
        :return:
        """
        print("Изделие требует деликатной стирки (предпочтительно ручной уход). Не стирать в воде с температурой выше 40 градусов! ")


if __name__ == "__main__":
    clothes_1 = Clothes("Gucci", "F", 40)
    print(clothes_1)
    print(repr(clothes_1))
    clothes_1.conversion_to_international_size()
    clothes_1.washing_mode_information()

    clothes_2 = ClothesFromDelicateFabric("Gucci", "m", 50, "Лён")
    print(clothes_2)
    print(repr(clothes_2))
    clothes_2.conversion_to_international_size()
    clothes_2.washing_mode_information()
    pass
