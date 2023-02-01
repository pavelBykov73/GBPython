# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
#
# 10 -> 1 2 4 8
#
# пользователь будет вводить каждое число на новой строке для задач 10, 12.

def input_int_value(msg):
    input_correct = False
    while not input_correct:
        try:
            val = int(input(msg))
            input_correct = True
        except ValueError:
            print("Неверный ввод!")
            # exit(-1)
    return val


def input_positive_value(msg):
    while True:
        val = input_int_value(msg)
        if val >= 0:
            break
        else:
            print("Ожидается положительное число!")
    return val


n = input_positive_value("Введите число N:")
exp = 0
value = pow(2, exp)
print(f"Ответ:")
while value < n:
    print(f"{value} ")
    exp += 1
    value = pow(2, exp)
