# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
#
# 5 -> 1 0 1 1 0
# 2

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


n = input_int_value("Введите количество монет:")
sum0 = 0
sum1 = 0
print(f"Введите положение монеток на столе (1 - решка, 0 - орел):")
for i in range(n):
    value_correct = False
    while not value_correct:
        val = input_int_value(f"{i}>")
        if val == 0:
            sum0 += 1
            value_correct = True
        elif val == 1:
            sum1 += 1
            value_correct = True
        else:
            print("Неверный ввод!")

if sum0 <= sum1:
    print(f"Надо перевернуть орлов (0). Количество таких монет: {sum0}")
else:
    print(f"Надо перевернуть решки (1). Количество таких монет: {sum1}")
