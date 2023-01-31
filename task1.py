class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    """ Бумажная книга, дочерний класс книги """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError('Число страниц должено быть положительным целочисленным типом данных')
        if value <= 0:
            raise ValueError('Число страниц не может быть отрицательным')

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}," \
               f"pages={self.pages!r})"


class AudioBook(Book):
    """ Аудио книга, дочерний класс книги """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError('Должно быть положительным чяислом с плавающей точкой')
        if value <= 0:
            raise ValueError('Длительность аудиокниги не может быть отрицательым числом')

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}," \
               f"duration={self.duration!r})"
