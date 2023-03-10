"""
Решение задачи № 24 Семинара 4:
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

4 -> 1 2 3 4
9
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


def max_sum_3_nearest(lst):
    """
    Нахождение максимального значения суммы 3 рядом стоящих элементов,
    считая, что это кольцо
    По индексам
    :param lst: список значений
    :return: максимальное значение суммы
    """
    maximum = 0
    for i, val in enumerate(lst):
        sum_3 = lst[i] + lst[i - 1] + lst[i - 2]
        if maximum < sum_3:
            maximum = sum_3
    return maximum


numbers_1 = input_list_1("Введите список урожайности кустов грядки:", lambda x: int(x))
print(f"Список: {numbers_1}")
print(f"Максимальное число ягод за заход: {max_sum_3_nearest(numbers_1)}")
