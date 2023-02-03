"""
Модуль решения задачи № 1 Урока 3:
Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""


def input_int_value(msg):
    """
    Ввод целого числа с консоли. В случае ошибки ввода выполняется повтор
    кроме ввода пустой строки
    :param msg: сообщение приглашения ввода
    :return: None - ввод отменен, либо целое число
    """
    input_correct = False
    while not input_correct:
        try:
            in_str = input(msg)
            if in_str == "":
                return None
            val = int(in_str)
            input_correct = True
        except ValueError:
            print("Неверный ввод!")
            # exit(-1)
    return val


def input_list(msg):
    """
    Ввод целочисленного списка с консоли
    :param msg: Сообщение перед вводом списка
    :return: список целых чисел
    """
    print(msg)
    numbers = []
    while True:
        in_val = input_int_value(">")
        if in_val is None:
            return numbers
        numbers.append(in_val)


numbers = input_list("Введите список целых чисел (пустой ввод - завершение списка):")
print(numbers)
summa = 0
for i in numbers[1::2]:
    summa += i
print(f"Сумма элементов списка на нечетных позициях = {summa}")
