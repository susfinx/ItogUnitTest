
from calc_aver.average_module import Average

def test_compare_averages():
    """
    Тест для сравнения средних значений списков.
    """
    comparator = Average()

    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]

    result = comparator.compare_averages(list1, list2)
    assert result == "Второй список имеет большее среднее значение"

def test_compare_averages_equal():
    """
    Тест для сравнения средних значений списков, когда они равны.
    """
    comparator = Average()

    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 4, 3, 2, 1]

    result = comparator.compare_averages(list1, list2)
    assert result == "Средние значения равны"

def test_compare_averages_empty_lists():
    """
    Тест для сравнения средних значений при пустых списках.
    """
    comparator = Average()

    list1 = []
    list2 = [1, 2, 3, 4, 5]

    result = comparator.compare_averages(list1, list2)
    assert result == "Второй список имеет большее среднее значение"

def test_compare_averages_different_lengths():
    """
    Тест для сравнения средних значений при разной длине списка.
    """
    comparator = Average()

    list1 = [1, 2, 3]
    list2 = [4, 5, 6, 7, 8]

    result = comparator.compare_averages(list1, list2)
    assert result == "Второй список имеет большее среднее значение"

def test_compare_averages_negative_numbers():
    """
    Тест для сравнения средних значений с отрицательными числами.
    """
    comparator = Average()

    list1 = [-1, -2, -3]
    list2 = [1, 2, 3]

    result = comparator.compare_averages(list1, list2)
    assert result == "Второй список имеет большее среднее значение"

def test_compare_averages_mixed_types():
    """
    Тест для сравнения средних значений смешанных типов данных.
    """
    comparator = Average()

    list1 = [1, 2, 3]
    list2 = [1, 2, "3"]

    result = comparator.compare_averages(list1, list2)
    assert result == "Список содержит элементы неподходящего типа"


