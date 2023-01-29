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
        if isinstance(pages, int):
            if pages > 0:
                self._pages = pages
            else:
                raise AttributeError(f'Неправильное число страниц книги: {pages!r}')
        else:
            raise AttributeError(f'Кол-во страниц должно быть положительным целочисленным числом')

    def __str__(self) -> str:
        return f"{super().__str__()} Кол-во страниц: {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}," \
               f"pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages


class AudioBook(Book):
    """ Аудио книга, дочерний класс книги """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, float):
            if duration > 0:
                self._duration = duration
            else:
                raise AttributeError(f'Неправильная длительность книги: {duration!r}')
        else:
            raise AttributeError(f'Длительность должна быть положительным числом с плавающей точкой')

    def __str__(self) -> str:
        return f"{super().__str__()} Длительность аудиокниги: {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}," \
               f"duration={self.duration!r})"

    @property
    def duration(self) -> float:
        return self._duration
