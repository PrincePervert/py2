if __name__ == "__main__":
    class Student:
        def __init__(self, name: str, year: int):
            """
            Создание и подготовка к работе класса "Студент"
            name: Имя студента
            year: Год обучения студента
            """
            self._name = name
            self._year = year
        """Параметры name и year изменяться не могут, сделаем их непубличными"""

        @property
        def name(self) -> str:
            return self._name

        @property
        def year(self) -> int:
            return self._year

        @year.setter
        def year(self, value: int) -> None:
            if not isinstance(value, int):
                raise ValueError('Год обучения должен быть положительным целочисленным типом данных')
            if value <= 0:
                raise ValueError('Год обучения не может быть отрицательным')

        def avg_score(self) -> float:
            ...
        """Метод подсчёта среднего балла студента"""

        def publications(self) -> int:
            ...
        """Метод, рассчитывающий количество научных публикаций студента"""

        def __str__(self) -> str:
            return f"Студент {self.name}. Год обучения: {self.year}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, year={self.year!r}"


    class Bachelor(Student):
        def __init__(self, name: str, year: int, supervisor: str):
            """
            Создание и подготовка к работе дочернего класса "Бакалавр"
            supervisor: Имя научного руководителя студента
            """
            super().__init__(name, year)
            self.supervisor = supervisor

        def publications(self) -> int:
            ...
        """
        Метод, рассчитывающий количество научных публикаций студента за время
        учёбы в бакалавриате, учитывается новый аргумент (научный руководитель),
        поэтому метод перегружается.
        """

        def __str__(self) -> str:
            return f"Студент-бакалавр {self.name}. Год обучения: {self.year}. " \
                   f"Научный руководитель: {self.supervisor}."

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, year={self.year!r}, " \
                   f"supervisor={self.supervisor!r}"
