"""
Решение задачи № 30 Семинара 6:
Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
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


def generate_ariphmetic_list(start, step, cnt):
    """
    Формирование списка (массива) элементов арифметической прогрессии
    :param start: начальный элемент
    :param step: шаг
    :param cnt: число элементов
    :return: массив
    """
    numbers = []
    for i in range(0, cnt):
        numbers.append(start + i * step)
    return numbers


start_value = input_value("Введите начальное значение:", lambda x: float(x))
delta = input_value("Введите шаг арифметической прогрессии:", lambda x: float(x))
count = input_value("Введите количество элементов:", lambda x: abs(int(x)))
ariphm_progr = generate_ariphmetic_list(start_value, delta, count)
print(f"Список чисел арифметической прогрессии: {ariphm_progr}")
