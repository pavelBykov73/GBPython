"""
Решение задачи № 22 Семинара 4:
Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
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


numbers1 = input_list_1("Введите список 1 целых чисел (пустой ввод - завершение списка):", lambda x: int(x))
print(f"Набор 1: {numbers1}")
numbers2 = input_list_1("Введите список 2 целых чисел (пустой ввод - завершение списка):", lambda x: int(x))
print(f"Набор 2: {numbers2}")
set_1 = set(numbers1)
print(f"Множество 1: {set_1}")
set_2 = set(numbers2)
print(f"Множество 2: {set_2}")
intersection = list(set_1.intersection(set_2))
intersection.sort()
print(f"Упорядоченное пересечение множеств: {intersection}")
