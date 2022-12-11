import doctest


class Oak:
    def __init__(self, number_of_branches: int, number_of_leaves: int):
        """
        Создание и подготовка к работе объекта "Дуб"
        :param number_of_branches: Количество веток
        :param number_of_leaves: Количество листьев
        Примеры:
        >>> oak = Oak(20, 12000)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_branches, int):
            raise TypeError("Количество веток должно быть типа int")
        if number_of_branches < 0:
            raise ValueError("Количество веток должно быть неотрицательным числом")
        self.number_of_branches = number_of_branches

        if not isinstance(number_of_leaves, int):
            raise TypeError("Количество листьев должно быть типа int")
        if number_of_branches < 0:
            raise ValueError("Количество листьев должно быть неотрицательным числом")
        self.number_of_leaves = number_of_leaves

    def is_it_winter(self) -> bool:
        """
        Функция которая проверяет идёт ли сейчас зима(Есть ли листья?)
        :return: Зима ли сейчас?
        Примеры:
        >>> oak = Oak(60, 0)
        >>> oak.is_it_winter()
        """
        ...

    def avg_leaves_per_branch(self) -> float:
        """
        Функция которая считает среднее число листьев на ветке дуба
        :return: Среднее число листьев на ветке
        Примеры:
        >>> oak = Oak(60, 8000)
        >>> oak.avg_leaves_per_branch()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        """
        Создание и подготовка к работе объекта "Треугольник"
        :param a: Длина первой стороны треугольника
        :param b: Длина второй стороны треугольника
        :param c: Длина последней стороны треугольника
        Примеры:
        >>> triangle = Triangle(4, 3, 6) #инициализация экземпляра класса
        """
        if not isinstance(a, (int, float)):
            raise TypeError("Длина стороны треугольника должна быть типа int или float")
        if a <= 0:
            raise TypeError("Длина стороны треугольника должна быть положительным числом")
        if a > b + c:
            raise TypeError("Длина стороны треугольника не может быть больше суммы длин двух других сторон")
        self.a = a

        if not isinstance(b, (int, float)):
            raise TypeError("Длина стороны треугольника должна быть типа int или float")
        if b <= 0:
            raise TypeError("Длина стороны треугольника должна быть положительным числом")
        if b > a + c:
            raise TypeError("Длина стороны треугольника не может быть больше суммы длин двух других сторон")
        self.b = b

        if not isinstance(c, (int, float)):
            raise TypeError("Длина стороны треугольника должна быть типа int или float")
        if c <= 0:
            raise TypeError("Длина стороны треугольника должна быть положительным числом")
        if c > a + b:
            raise TypeError("Длина стороны треугольника не может быть больше суммы длин двух других сторон")
        self.c = c

    def triangle_perimeter(self) -> float:
        """
        Функция расчёта периметра треугольника
        :return: Периметр треугольника
        Примеры:
        >>> triangle = Triangle(4, 3, 6)
        >>> triangle.triangle_perimeter()
        """
        ...

    def triangle_square(self) -> float:
        """
        Функция расчёта площади треугольника
        :return: Площадь треугольника
        Примеры:
        >>> triangle = Triangle(4, 3, 6)
        >>> triangle.triangle_square()
        """
        ...


class Sleep:
    def __init__(self, sleep_duration: float, viewed_dreams: float):
        """
        Создание и подготовка к работе объекта "Сон"
        :param sleep_duration: Продолжительность сна
        :param viewed_dreams: Число сновидений за сон
        Примеры:
        >>> sleep = Sleep(8, 1) #инициализация экземпляра класса
        """
        if not isinstance(sleep_duration, (int, float)):
            raise TypeError("Продолжительность сна должна быть типа int или float")
        if sleep_duration < 0:
            raise TypeError("Продолжительность сна должна быть неотрицательным числом")
        self.sleep_duration = sleep_duration

        if not isinstance(viewed_dreams, (int, float)):
            raise TypeError("Число сновидений за сон должно быть типа int или float")
        if viewed_dreams < 0:
            raise TypeError("Число сновидений за сон должно быть неотрицательным числом")
        self.viewed_dreams = viewed_dreams

    def avg_dream_duration(self) -> float:
        """
        Функция которая считает среднюю продолжительность сновидений
        :return: Средняя продолжительность сновидений
        Примеры:
        >>> sleep = Sleep(8, 2)
        >>> sleep.avg_dream_duration()
        """
        ...

    def only_black_void(self) -> bool:
        """
        Функция, которая проверяет, видит ли вообще человек сны
        :return: Видит ли человек сны
        Примеры:
        >>> sleep = Sleep(8, 0)
        >>> sleep.only_black_void()
        """
        ...
