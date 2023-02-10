"""
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4
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


def my_sum(a, b):
    """
    Сумма с помощью рекурсии,
    :param a: число 1
    :param b: число 2
    :return: результат
    """
    if b <= 0:
        return a
    return 1 + my_sum(a, b - 1)


number1 = input_value("Введите число 1 (натуральное):", lambda x: abs(int(x)))
number2 = input_value("Введите число 2 (натуральное):", lambda x: abs(int(x)))
print(f"Результат {number1} + {number2}: {my_sum(number1, number2)}")
