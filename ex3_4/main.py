"""
Решение задачи № 4 Семинара 3:
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
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


def number2bin(n):
    """
    Преобразование числа в список битов
    :param n: Число
    :return: список
    """
    bits = []
    while n > 0:
        bits.insert(0, n % 2)
        n //= 2
    return bits


number = input_value("Введите число:", lambda x: int(x))
out_list = number2bin(number)
print(f"Result (method 1): {out_list}")
print(f"Result (method 2): {bin(number)}")
print(f"Result (method 3): {number:08b}")
