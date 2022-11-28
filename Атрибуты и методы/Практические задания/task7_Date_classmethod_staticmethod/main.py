class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    def is_leap_year(self, year: int):
        """Проверяет, является ли год високосным"""
        ...

    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        ...

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        ...
