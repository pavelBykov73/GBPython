"""
Решение задачи № 26 Семинара 5:
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
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


def my_pow(num, pow_val):
    """
    Возведение в степень с помощью рекурсии,
    :param num: число
    :param pow_val: степень
    :return: результат
    """
    if pow_val == 0:
        return 1
    return num * my_pow(num, pow_val - 1)


number = input_value("Введите число:", lambda x: int(x))
pow_value = input_value("Введите степень (натуральное число):", lambda x: abs(int(x)))
print(f"Результат {number}^{pow_value}: {my_pow(number, pow_value)}")
