"""
Решение задачи № 5 Семинара 3:
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
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


def neg_fibonacci(count):
    """
    Формирование списка чисел фибоначи включая отрицательные индексы
    :param count: количество чисел (положительных)
    :return: список чисел
    """
    out = [1, 0, 1]
    for i in range(1, count):
        f_n = out[-1] + out[-2]
        out.append(f_n)
        out.insert(0, f_n * pow(-1, i))
    return out


number = input_value("Введите число:", lambda x: abs(int(x)))
out_list = neg_fibonacci(number)
print(f"Result: {out_list}")
