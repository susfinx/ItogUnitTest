
class Average:
    """
    Класс для вычисления среднего значения и сравнения средних значений списков.
    """

    def calculate_average(self, numbers):
        """
        Вычисляет среднее значение чисел в списке.

        :param numbers: Список чисел.
        :return: Среднее значение.
        """
        if not numbers:
            return 0
        try:
            return sum(numbers) / len(numbers)
        except TypeError:
            raise ValueError("Список содержит элементы неподходящего типа")

    def compare_averages(self, list1, list2):
        """
        Сравнивает средние значения двух списков и возвращает результат сравнения.

        :param list1: Первый список чисел.
        :param list2: Второй список чисел.
        :return: Результат сравнения.
        """
        try:
            avg1 = self.calculate_average(list1)
            avg2 = self.calculate_average(list2)
        except ValueError as e:
            return str(e)

        if avg1 is not None and avg2 is not None:  # Изменение здесь
            if avg1 > avg2:
                return "Первый список имеет большее среднее значение"
            elif avg2 > avg1:
                return "Второй список имеет большее среднее значение"
            else:
                return "Средние значения равны"
        else:
            return "Один из списков содержит элементы неподходящего типа"
