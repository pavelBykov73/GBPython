"""
Решение задачи № 32 Семинара 6:
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""


def input_value(msg, type):
    """
    Ввод числа с консоли. В случае ошибки ввода выполняется повтор
    кроме ввода пустой строки
    :param msg: сообщение приглашения ввода
    :param type: лямбда функция преобразования типа данных
    :return: None - ввод отменен, либо число
    """
    input_correct = False
    while not input_correct:
        try:
            in_str = input(msg)
            if in_str == "":
                return None
            val = type(in_str)
            input_correct = True
        except ValueError:
            print("Неверный ввод!")
            # exit(-1)
    return val


def input_list(msg, type):
    """
    Ввод списка с консоли
    :param msg: Сообщение перед вводом списка
    :param type: лямбда функция преобразования типа данных
    :return: список чисел
    """
    print(msg)
    numbers = []
    while True:
        in_val = input_value(">", type)
        if in_val is None:
            return numbers
        numbers.append(in_val)


def input_list_1(msg, type):
    """
    Ввод списка с консоли в строке через пробел
    :param msg: Сообщение перед вводом списка
    :param type: лямбда функция преобразования типа данных
    :return: список чисел
    """
    print(msg)
    input_correct = False
    while not input_correct:
        try:
            numbers = [type(s) for s in input().split()]
            input_correct = True
        except ValueError:
            print("Неверный ввод! Повторите:")
    return numbers


def range_indexes(arr, min, max):
    """
    Формирование списка индексов элементов массива в диапазоне между min и max
    :param min:
    :param max:
    :param arr: массив элементов
    :return: массив
    """
    idx = []
    for i, val in enumerate(arr):
        if min <= val <= max:
            idx.append(i)
    return idx


numbers = input_list_1("Введите список чисел:", lambda x: float(x))
print(f"Список: {numbers}")
min_value = input_value("Введите минимальное значение:", lambda x: float(x))
max_value = input_value("Введите максимальное значение:", lambda x: float(x))
range_index = range_indexes(numbers, min_value, max_value)
print(f"Список индексов элементов больше {min_value} и меньше {max_value}: {range_index}")
