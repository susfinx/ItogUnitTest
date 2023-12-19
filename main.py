from calc_aver.average_module import Average

if __name__ == "__main__":
    comparator = Average()

    list1 = [1, 2, 3, 30, 15]
    list2 = [6, 7, 8, 9, 10]

    result = comparator.compare_averages(list1, list2)
    print(result)
