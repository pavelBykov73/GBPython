"""
Решение задачи № 2 Семинара 3:
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
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
out_list = []
# этот вариант работает только с парами элементов,
# если массив с нечетной длиной, то средний элемент не попадает в расчет
# for i in range(len(numbers) // 2):

# этот вариант позволяет корректно округлить (+0.2 для исключения "банковского" округления),
# чтобы для массива с нечетной длиной суммировать средний элемент
for i in range(round(len(numbers) / 2 + 0.2)):
    out_list.append(numbers[i] * numbers[-i - 1])
print(f"Произведения пар элементов списка = {out_list}")
