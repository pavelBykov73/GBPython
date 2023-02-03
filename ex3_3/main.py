"""
Решение задачи № 3 Семинара 3:
Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""


def input_value(msg, type):
    """
    Ввод числа с консоли. В случае ошибки ввода выполняется повтор
    кроме ввода пустой строки
    :param msg: сообщение приглашения ввода
    :param type: лямбда функция преобразования типа данных
    :return: None - ввод отменен, либо целое число
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
    :return: список целых чисел
    """
    print(msg)
    numbers = []
    while True:
        in_val = input_value(">", type)
        if in_val is None:
            return numbers
        numbers.append(in_val)


numbers = input_list("Введите список целых чисел (пустой ввод - завершение списка):", lambda x: float(x))
print(f"Исходный список: {numbers}")
for i, item in enumerate(numbers):
    numbers[i] = round(abs(numbers[i] - int(numbers[i])), 3)
print(f"Список дробных частей: {numbers}")
print(f"Разность максимальной и минимальной дробной части: {max(numbers) - min(numbers)}")
