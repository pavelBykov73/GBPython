# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
# за проезд и получали билет с номером. Счастливым билетом называют такой билет
# с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

def sum_digit(num):
    sum_of_digit = 0
    while num > 0:
        sum_of_digit += num % 10
        num //= 10
    return sum_of_digit


print("Введите шестизначный номер билета:")
try:
    number = int(input())
except ValueError:
    print("Неверный ввод!")
    exit(-1)

if 0 <= number <= 999999:
    left_num = number // 1000
    right_num = number % 1000

    if sum_digit(left_num) == sum_digit(right_num):
        print(f"Билет с номером {number:06} счастливый!")
    else:
        print(f"Увы, билет с номером {number:06} не счастливый!")
else:
    print("В билете должно быть 6 цифр и номер должен быть больше 0")


